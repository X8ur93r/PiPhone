#!/bin/python3

import importlib
import debug
import tools.json
from apps import apps

class kernel:
    def __init__(self):
        self.DRIVER         = {}
        self.INTERFACES     = {}
    def loadDriver(self,driver):
        try:
            self.DRIVER[driver] = importlib.import_module(f'.{driver}', 'driver')
            debug.info(f'loaded the driver:{driver}','kernel::loadDriver')
        except Exception as e:
            debug.debug('kernel::loadDriver', e, f'could not load the driver:{driver}', False)
            return False
        return True
    def reloadDriver(self,driver):
        try:
            importlib.reload(self.DRIVER[driver])
        except Exception as e:
            debug.debug('kernel::reloadDriver', e, f'could not reload the driver:{driver}', False)
            return False
        return True
    def loadDrivers(self):
        driver = tools.json.json2dict('settings/driver.json')
        for d in driver:
            self.loadDriver(d)
            if driver[d] not in self.INTERFACES:
                self.INTERFACES[driver[d]] = self.DRIVER[d].IF()
    def reloadDrivers(self):
        driver = tools.json.json2dict('settings/driver.json')
        for d in driver:
            self.reloadDriver(d)
    def main(self):
        self.loadDrivers()
        self.INTERFACES["APPIF"] = apps.APPIF()
        self.INTERFACES["APPIF"].loadApps()
    def cleanup(self):
        self.INTERFACES["APPIF"].cleanup()
        self.INTERFACES.pop("APPIF")
        for INF in self.INTERFACES:
            self.INTERFACES[INF].cleanup()
            self.INTERFACES.pop(INF)

k = kernel()
k.loadDrivers()
print(k.INTERFACES)
print(k.DRIVER)
