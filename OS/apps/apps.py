###################
# app manager     #
# author: x8ur93r #
###################

import importlib
import tools.json
import debug

class APPIF:
    def __init__(self):
        self.APPS={}
        self.DEFAULTAPPS=tools.json.json2dict('settings/defaultApps.json')
        self.KERNEL=None
    def loadApp(self,appname):
        if not appname in self.APPS:
            self.APPS[appname] = importlib.import_module(f'.{appname}', 'apps')
    def loadApps(self):
        apps = tools.json.json2dict('settings/apps.json')
        for app in apps:
            self.loadApp(app)
    def addApp(self,appname, describtion):
        apps = tools.json.json2dict('settings/apps.json')
        apps[appname] = describtion
        tools.json.dict2json(apps,'settings/app.json')
    def getAppKwargs(self,appname):
        return self.APPS[appname].kwargs
    def runApp(self,appname):
        _INTERFACES = {}    # interfaces:       necassary
        _N_APPS = {}        # apps:             necessary
        _NN_APPS = {}       # apps:         not necessary
        # transform DEFAULTAPPNAME to APPNAME if the appname var is the name of a default app
        if appname in self.DEFAULTAPPS:
            appname = self.DEFAULTAPPS[appname]
        # check if the app exist
        if not appname in self.APPS:
            debug.debug('APPIF::runApp()',f'app {appname} does not exist', t='i')
            return
        # get necessary interfaces
        for _INF in self.APPS[appname].INTERFACES:
            if _INF in self.KERNEL.INTERFACES:
                _INTERFACES[_INF] = self.KERNEL.INTERFACES[_INF]
            else:
                debug.debug('APPIF:runApp()', f'interface {_INF} does not exist in kernel.INTERFACES')
                return
        # get necessary apps
        for _N_APP in self.APPS[appname].N_APPS:
            if _N_APP in self.APPS:
                _N_APPS[_N_APP] = self.APPS[_N_APP]
            else:
                debug.debug('APPIF:runApp()', f'app {_N_APP} does not exist')
                return
        # get not necessary apps
        for _NN_APP in self.APPS[appname].NN_APPS:
            if _NN_APP in self.APPS:
                _NN_APPS[_NN_APP] = self.APPS[_NN_APP]
            else:
                debug.debug('APPIF:runApp()', f'app {_NN_APP} does not exist',t='i')
        # run
        self.APPS[appname].app.run(_INTERFACES,_N_APPS,_NN_APPS)
    def main(self):
        self.loadApps()
        print("apps.py's main() func")
        self.runApp("KEYBOARD")
        print("end of apps.py's main() func")
    def cleanup(self):
        for app in list(self.APPS.keys()):
            # fix this
            self.APPS[app].app.cleanup()
            self.APPS.pop(app)
