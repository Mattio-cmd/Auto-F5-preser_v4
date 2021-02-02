import time
import pyautogui
time.sleep(10)
i = 25
j = 0
k = 3
while i != 0:
    j += 1
    i = i - k
    pyautogui.press("F5")
    time.sleep(7)
