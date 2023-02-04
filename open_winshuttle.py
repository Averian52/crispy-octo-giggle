import os
import pyautogui
import time

def openFile():    
    path = "C://Users//R.MARTIN//Documents//Python - Project code//Test Files//FBL3N_OPEN_ITEMS_BYUK.xlsx"
    path = os.path.realpath(path)
    os.startfile(path)
    time.sleep(1)

def fullScreen():    
    pyautogui.hotkey('win', 'up')
    time.sleep(1)

def findAndClickRibbon():    
    pyautogui.moveTo(550, 50)
    pyautogui.click()
    time.sleep(1)

def runAddIn():    
    pyautogui.moveTo(15, 100)
    pyautogui.click()
    time.sleep(1)

def saveFile():    
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)

def closeFile():    
    pyautogui.hotkey('alt', 'f4')
    time.sleep(1)

openFile()
fullScreen()


#findAndClickRibbon()
#runAddIn()
#saveFile()
#closeFile()