import time
import pyautogui


time.sleep(5)
pyautogui.moveTo(x=1967,y=1279)
pyautogui.click()

pyautogui.moveTo(x=2204,y=1363)
pyautogui.click()

pyautogui.moveTo(x=1967,y=1279)
pyautogui.click()

pyautogui.moveTo(x=2200,y=1440)
pyautogui.click()

while True:
    print (pyautogui.position())
    time.sleep(3)















