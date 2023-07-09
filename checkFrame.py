from PIL import ImageGrab
import pyautogui
from PIL import Image
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 
pytesseract.pytesseract.tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'
from giveCords import *
import re
from giveColors import *

def isColorInFrame(target_color, CordsArray):
    image = ImageGrab.grab(bbox=(CordsArray[0], CordsArray[1], CordsArray[2], CordsArray[3]))
    image_array = np.array(image)
    target_red, target_green, target_blue = target_color
    height, width, _ = image_array.shape
    for y in range(height):
        for x in range(width):
            pixel = image_array[y, x]
            red, green, blue = pixel

            if red == target_red and green == target_green and blue == target_blue:
                return True

    return False

def read_text_from_image(CordsArray):
    # Bild öffnen
    image = ImageGrab.grab(bbox=(CordsArray[0], CordsArray[1], CordsArray[2], CordsArray[3]))
    # Schrift auslesen
    config = '--oem 3 --psm 6 -l deu'
    text = pytesseract.image_to_string(image, config=config)
    return text

def getEnemyStats(text):
    lp_match = re.search(r"LP: (\d+)", text)
    print(text)
    if lp_match:
        lp_value = lp_match.group(1)
        print(f"LP: {lp_value}")
    else:
        print("LP wurde nicht gefunden.")

    angriff_match = re.search(r"Angriffsstärke: (\d+)", text)
    if angriff_match:
        angriff_value = angriff_match.group(1)
        print(f"Angriffsstärke: {angriff_value}")
    else:
        print("Angriffsstärke wurde nicht gefunden.")
        angriff_value = "10000000"
    
    return lp_value , angriff_value

def isKillable(text):
    lp_value, angriff_value = getEnemyStats(text)
    if lp_value and angriff_value :
        if(lp_value and angriff_value):
            if(int(lp_value) <= 100) and int(angriff_value) <= 30:
                return True
    
    LP, AP , VS = getStats()
    
    return False

def isEnemy():
    image = ImageGrab.grab(bbox=giveFieldforTextField())
    text = read_text_from_image(giveFieldforTextField())
    text_data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
    for i, word in enumerate(text_data['text']):
        # Wenn das Wort gefunden wurde, die Koordinaten zurückgeben
        if word.strip() == "Schnellangriff":
            print("Gefunden")
            x = text_data['left'][i] + giveFieldforTextField()[0]
            y = text_data['top'][i] + giveFieldforTextField()[1]
            position=[x,y]
            pyautogui.moveTo(position, duration=0)
            if isKillable(text):
                pyautogui.click()
    return


def isItem():
    image = ImageGrab.grab(bbox=giveFieldforTextField())
    text = read_text_from_image(giveFieldforTextField())
    text_data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
    for i, word in enumerate(text_data['text']):
        # Wenn das Wort gefunden wurde, die Koordinaten zurückgeben
        if word.strip() == "Nehmen":
            x = text_data['left'][i] + 55 
            y = text_data['top'][i] + 410
            position=[x,y]
            pyautogui.moveTo(position, duration=0)
            pyautogui.click()
            print (position)
    return

def isTimeToMove():
    return not isColorInFrame(TimerColor(), giveFieldTimer())

def getStats():
    image = ImageGrab.grab(bbox=giveFieldStats())
    text = read_text_from_image(giveFieldforTextField())
    LP = getPlayerLP(text)
    AP = getPlayerAP(text)
    VS = getPlayerVS(text)
    return [LP,AP,VS]

def getPlayerLP(text):
    pattern = r"Lebenspunkte: \((\d+)/(\d+)\)"
    LP = re.search(pattern, text)
    if LP:
        current_hp = int(LP.group(1)) 
        max_hp = int(LP.group(2))
        return current_hp

def getPlayerAP(text):
    pattern = r"Angriffsstärke: (\d+) \+(\d+)"
    AP = re.search(pattern, text)
    if AP:
        base_attack = int(AP.group(1))  
        bonus_attack = int(AP.group(2))
        
        return base_attack + bonus_attack
    
def getPlayerVS(text):
    pattern = r"Verteidigungsstärke: (\d+) \+(\d+)"
    VS = re.search(pattern, text)
    if VS:
        base_defense = int(VS.group(1))  
        bonus_defense = int(VS.group(2))
        return base_defense + bonus_defense
