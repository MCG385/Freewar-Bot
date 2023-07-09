  
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

def movement():
    lastMoves = ["Upper"]
    is_moved = False
    while not is_moved:
        direction = random.randint(1, 4) 
        # movement
        
        
        
        
        if direction == 1:
            pyautogui.moveTo(givePointToUpperField(), duration=0)
            if not isColorInFrame(NoGoAreaColor(), giveFieldOfUpperField()):
                if lastMoves[0] == "Lower":
                    pyautogui.click()
                    is_moved = True
                    lastMoves.append("Upper")
        elif direction == 2:
            pyautogui.moveTo(givePointToRightField(), duration=0)
            if not isColorInFrame(NoGoAreaColor(), giveFieldOfRightField()):
                if lastMoves[0] == "Left":
                    pyautogui.click()
                    is_moved = True
                    lastMoves.append("Right")
        elif direction == 3:
            pyautogui.moveTo(givePointToLowerField(), duration=0)
            if not isColorInFrame(NoGoAreaColor(), giveFieldOfLowerField()):
                if lastMoves[0] == "Upper":
                    pyautogui.click()
                    is_moved = True
                    lastMoves.append("Lower")
        elif direction == 4:
            pyautogui.moveTo(givePointToLeftField(), duration=0)
            if not isColorInFrame(NoGoAreaColor(), giveFieldOfLeftField()):
                if lastMoves[0] == "Right":
                    pyautogui.click()
                    is_moved = True
                    lastMoves.append("Left")
