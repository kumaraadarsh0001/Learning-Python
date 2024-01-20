#if you want to send same word in many time
#than you can use this code 
import pyautogui
import time
time.sleep(5)   #it will take 5 sec and then print 1 by 1 
n=50            #this is the limit as you want
for i in range(n):
    pyautogui.typewrite('hellow my dear friend')
    pyautogui.press('enter')