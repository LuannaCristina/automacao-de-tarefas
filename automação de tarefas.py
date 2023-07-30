import pyautogui
import time

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3) 
  
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=638, y=368)
pyautogui.write("luannaandradeee@hotmail.com")
pyautogui.press("tab")
pyautogui.write("123s2")
pyautogui.click(x=676, y=531)
time.sleep(3)

import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    print(linha)
    pyautogui.click(x=632, y=246)
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    obs = tabela.loc[linha, "obs"]

    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")


    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)








