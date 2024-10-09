import pyautogui
import time 
import pandas 

pyautogui.PAUSE= 1.0

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

tabela = pandas.read_csv("produtos.csv")
print(tabela)

linha=0
for linha in tabela.index:
    pyautogui.click(x=545, y=260)
    
    codigo= tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca= tabela.loc[linha,"marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo= tabela.loc[linha,"tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preço = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preço))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs= tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll("10000")