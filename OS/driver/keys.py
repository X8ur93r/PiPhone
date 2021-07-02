###################
# key interface   #
# author: x8ur93r #
###################

import RPi.GPIO as GPIO

class INTERFACE:
    def __init__(self):
        # key pins (GPIO)
        self.KEYPINS = {
            'UP':       6,
            'DOWN':     19,
            'LEFT':     5,
            'RIGHT':    26,
            'MIDDLE':   13,
            '1':        21,
            '2':        20,
            '3':        16
        }
        # state of the keys
        self.KEYSTATES = {
            'UP':       0,
            'DOWN':     0,
            'LEFT':     0,
            'RIGHT':    0,
            'MIDDLE':   0,
            '1':        0,
            '2':        0,
            '3':        0
        }
        # (GPIO) init
        GPIO.setmode(GPIO.BCM) 
        GPIO.setup(self.KEYPINS['UP'],      GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.KEYPINS['DOWN'],    GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.KEYPINS['LEFT'],    GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.KEYPINS['RIGHT'],   GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.KEYPINS['MIDDLE'],  GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.KEYPINS['1'],       GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.KEYPINS['2'],       GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.KEYPINS['3'],       GPIO.IN, pull_up_down=GPIO.PUD_UP)
    def get(self,key):
        return self.KEYSTATES[key]
    def refresh(self):
        for key in self.KEYSTATES.keys():
            if GPIO.input(self.KEYPINS[key]) == 0:  self.KEYSTATES[key] = 0  # key released
            else:                                   self.KEYSTATES[key] = 1  # key pressed
    def cleanup(self):
        GPIO.cleanup()
