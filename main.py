  
from PIL import ImageGrab
import pyautogui
import random
import time
from PIL import Image
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 


from giveCords import *
from giveColors import *
from checkFrame import *
from movement import *

while False:
    # Mausposition abrufen
    x, y = pyautogui.position()
    #Position ausgeben
    
    
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((x, y))
    red, green, blue = pixel_color
    print(f"RGB: {red}, {green}, {blue}" ,x,y)
    # Weitere Anweisungen hier einfügen
    
    #text = read_text_from_image(giveFieldforTextField())
    #print(text)



def main():
    while True:
       
        isEnemy()
        isItem()  
        if(isTimeToMove()):
            movement()
        time.sleep(3)
        
        
main()
    
