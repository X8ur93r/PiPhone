###################
# gsm interface   #
# author: x8ur93r #
###################

import serial
import os

class INTERFACE:
    def __init__(self):
        self.GSM        = None
        self.DEVPATH    = "/dev/ttyUSB0"
        self.BAUDRATE   = 115200
        # init
        if os.path.isfile(self.DEVPATH):
            self.GSM        = serial.Serial(self.DEVPATH, self.BAUDRATE)
            self.GSM.flush()
    def write(self,data):
        self.GSM.write(data)
    def read(self):
        return self.GSM.read_all()
    def cleanup(self):
        pass