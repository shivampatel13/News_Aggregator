import pyautogui
import webbrowser as wb
import time
wb.open("https://web.whatsapp.com/")
time.sleep(10)
for i in range(100):
    pyautogui.press("v")
    pyautogui.press("a")
    pyautogui.press("c")
    pyautogui.press("h")
    pyautogui.press("a")
    pyautogui.press("v")
    pyautogui.press("a")
    pyautogui.press("space")
    pyautogui.press("b")
    pyautogui.press("e")
    pyautogui.press("s")
    pyautogui.press("h")
    pyautogui.press("space")
    pyautogui.press("enter")

