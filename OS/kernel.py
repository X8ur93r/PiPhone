#!/bin/python3

###################
# kernel          #
# author: x8ur93r #
###################

import importlib
import debug
import tools.json
from apps import apps

class kernel:
    def __init__(self):
        self.DRIVER         = {}
        self.INTERFACES     = {}
    def loadDriver(self,driverd,d):
        try:
            self.DRIVER[d] = importlib.import_module(f'.{d}', 'driver')
            # ,'kernel::loadDriver'
            debug.debug('kernel::loadDriver',f'loaded the driver \'{d}\'',t='+')
        except Exception as e:
            debug.debug('kernel::loadDriver',f'could not load the driver \'{d}\'',e,False)
            return False
        self.loadInterface(driverd,d)
        return True
    def reloadDriver(self,d):
        try:
            importlib.reload(self.DRIVER[d])
            debug.debug('kernel::reloadDriver',f'reloaded the driver \'{d}\'',t='+')
        except Exception as e:
            debug.debug('kernel::reloadDriver',f'could not reload the driver \'{d}\'',e,False)
            return False
        return True
    def loadInterface(self,driverd,d):
        if driverd not in self.INTERFACES:
            try:
                self.INTERFACES[driverd] = self.DRIVER[d].INTERFACE()
                debug.debug('kernel::loadInterface',f'loaded the Interface \'{driverd}\' from \'{d}\'', t='+')
            except Exception as e:
                debug.debug('kernel::loadInterface',f'could not load Interface \'{driverd}\' from \'{d}\'',e,False)
                return False
        return True
    def loadDrivers(self):
        driver = tools.json.json2dict('settings/driver.json')
        for d in driver:
            self.loadDriver(driver[d], d)
    def reloadDrivers(self):
        driver = tools.json.json2dict('settings/driver.json')
        for d in driver:
            self.reloadDriver(d)
    def main(self):
        self.loadDrivers()
        self.INTERFACES["APPIF"] = apps.APPIF()
        self.INTERFACES["APPIF"].KERNEL = self
        self.INTERFACES["APPIF"].main()
    def cleanup(self):
        self.INTERFACES["APPIF"].cleanup()
        self.INTERFACES.pop("APPIF")
        for INF in list(self.INTERFACES.keys()):
            self.INTERFACES[INF].cleanup()
            self.INTERFACES.pop(INF)

k = kernel()
k.main()
k.cleanup()
