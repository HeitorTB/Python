import pyautogui
import time 
import pandas 

pyautogui.PAUSE= 0.7

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=590, y=330)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

pyautogui.click(x=771, y=375)
pyautogui.write("heitortbr@gmail.com")
pyautogui.click(x=526, y=471)
pyautogui.write("heitortbr1234")
pyautogui.click(x=639, y=546)

tabela = pandas.read_csv("")
print(tabela)