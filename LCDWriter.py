import Adafruit_CharLCD as LCD

class LCDWriter(object):
    def __init__(self):

    def writeMessage(self):
        lcd.clear()
        lcd.message("test")

