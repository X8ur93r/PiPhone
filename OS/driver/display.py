#####################
# display interface #
# autor: x8ur93r    #
#####################

from . import LCD.LCD_1in44 as LCD_1in44
from . import LCD.LCD_Config as LCD_Config
from PIL import Image, ImageDraw

class DISPIF:
    def __init__(self):
        self.LCD            = LCD_1in44.LCD()
        self.LCD_SCAN_DIR   = LCD_1in44.L2R_U2D
        self.LCD_SIZE       = (128,128)
        self.BUFFER         = self.newIm()
        # init
        self.LCD_Init(self.LCD_SCAN_DIR)
        self.clear()
    def newIm(self,c='black',s=self.LCD_SIZE):
        return Image.New('RGB',s,c)
    def getDraw(self,img):
        return ImageDraw.Draw(img)
    def draw(self,x,y,*,img=None):
        if img is None:
            self.LCD.LCD_ShowImage(self.BUFFER,x,y)
        else:
            self.LCD.LCD_ShowImage(img,x,y)
    def clear(self):
        self.LCD.LCD_Clear()
    def cleanup(self):
        pass