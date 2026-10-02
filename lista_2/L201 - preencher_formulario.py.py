"""
Crie um CSV com nome, email e telefone de 10 pessoas e cadastre 
todas em um formulário de teste (o Google Forms serve), usando um laço for.
"""

import pyautogui
import pandas as pd
import time

link = "https://forms.gle/t3dJkWN82diPEP9i8"

tabela = pd.read_csv("pessoas.csv")

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

time.sleep(2)
pyautogui.write(link)
pyautogui.press("enter")

for linha in tabela.index:
    pyautogui.click(578, 543)
    pyautogui.write(str(tabela.loc[linha, "nome"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "email"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "telefone"]))
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.click(603, 362)