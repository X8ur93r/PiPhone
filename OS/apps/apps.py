##################
# app manager    #
# autor: x8ur93r #
##################

import importlib
import tools.json

class APPIF:
    def __init__(self):
        self.APPS={}
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
    def runApp(self,appname,**kwargs):
        self.APPS[appname].app.run()
    def cleanup(self):
        for app in self.APPS:
            self.APPS[app].app.cleanup()
            self.APPS.pop(app)
