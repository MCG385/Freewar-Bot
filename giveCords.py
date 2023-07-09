def giveFieldOfLocation():
    # Ausschnitt definieren
    left = 1674  # X-Koordinate der linken oberen Ecke des Ausschnitts
    top = 678    # Y-Koordinate der linken oberen Ecke des Ausschnitts
    right = 1746  # X-Koordinate der rechten unteren Ecke des Ausschnitts
    bottom = 752 # Y-Koordinate der rechten unteren Ecke des Ausschnitts

def giveFieldOfLowerField():
    # Ausschnitt definieren
    left_X = 1674 # X-Koordinate der linken oberen Ecke des Ausschnitts
    top_Y = 678  + 73  # Y-Koordinate der linken oberen Ecke des Ausschnitts
    right_X = 1746 # X-Koordinate der rechten unteren Ecke des Ausschnitts
    bottom_Y = 752 + 73# Y-Koordinate der rechten unteren Ecke des Ausschnitts     
    return [left_X, top_Y, right_X, bottom_Y]  

def giveFieldOfUpperField():
    left_X = 1674 # X-Koordinate der linken oberen Ecke des Ausschnitts
    top_Y = 678 - 73  # Y-Koordinate der linken oberen Ecke des Ausschnitts
    right_X = 1746 # X-Koordinate der rechten unteren Ecke des Ausschnitts
    bottom_Y = 752 - 73# Y-Koordinate der rechten unteren Ecke des Ausschnitts  
    return [left_X, top_Y, right_X, bottom_Y]  

def giveFieldOfLeftField():
    left_X = 1674 - 73 # X-Koordinate der linken oberen Ecke des Ausschnitts
    top_Y = 678 # Y-Koordinate der linken oberen Ecke des Ausschnitts
    right_X = 1746 - 73 # X-Koordinate der rechten unteren Ecke des Ausschnitts
    bottom_Y = 752# Y-Koordinate der rechten unteren Ecke des Ausschnitts  
    return [left_X, top_Y, right_X, bottom_Y]  

def giveFieldOfRightField():
    left_X = 1674+73 # X-Koordinate der linken oberen Ecke des Ausschnitts
    top_Y = 678 # Y-Koordinate der linken oberen Ecke des Ausschnitts
    right_X = 1746+73 # X-Koordinate der rechten unteren Ecke des Ausschnitts
    bottom_Y = 752# Y-Koordinate der rechten unteren Ecke des Ausschnitts  
    return [left_X, top_Y, right_X, bottom_Y]   

def giveFieldforTextField():
    left_X = 55 # X-Koordinate der linken oberen Ecke des Ausschnitts
    top_Y = 410 # Y-Koordinate der linken oberen Ecke des Ausschnitts
    right_X = 1500 # X-Koordinate der rechten unteren Ecke des Ausschnitts
    bottom_Y = 731# Y-Koordinate der rechten unteren Ecke des Ausschnitts  
    return [left_X, top_Y, right_X, bottom_Y]   

def giveFieldTimer():
    left_X = 1753 # X-Koordinate der linken oberen Ecke des Ausschnitts
    top_Y = 920 # Y-Koordinate der linken oberen Ecke des Ausschnitts
    right_X = 1852 # X-Koordinate der rechten unteren Ecke des Ausschnitts
    bottom_Y = 925# Y-Koordinate der rechten unteren Ecke des Ausschnitts  
    return [left_X, top_Y, right_X, bottom_Y]  

def giveFieldStats():
    left_X = 1499 # X-Koordinate der linken oberen Ecke des Ausschnitts
    top_Y = 107 # Y-Koordinate der linken oberen Ecke des Ausschnitts
    right_X = 1897 # X-Koordinate der rechten unteren Ecke des Ausschnitts
    bottom_Y = 495# Y-Koordinate der rechten unteren Ecke des Ausschnitts  
    return [left_X, top_Y, right_X, bottom_Y]  

def givePointToUpperField():
    x = 1700
    y = 640
    return[x,y]

def givePointToRightField():
    x = 1780
    y = 715
    return[x,y]
    
def givePointToLowerField():
    x = 1700
    y = 792
    return[x,y]

def givePointToLeftField():
    x = 1634
    y = 715
    return[x,y]

def givePointSchnellSchlag():
    x= 828
    y= 461
    return[x,y]

