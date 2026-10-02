"""
Com uma tabela de tarefas e prazos, abra o Bloco de Notas e escreva cada tarefa 
em uma linha, no formato "Tarefa: prazo". Salve o arquivo com o nome tarefas.txt.
"""


import pyautogui
import pandas as pd
import time

pyautogui.PAUSE = 1

tabela = pd.read_csv("tarefas.csv")

pyautogui.press("win")
pyautogui.write("bloco de notas")
pyautogui.press("enter")

for linha in tabela.index:
    tarefa = str(tabela.loc[linha, "tarefa"])
    prazo = str(tabela.loc[linha, "prazo"])
    pyautogui.write(f"{tarefa}: {prazo}" (interval=0.05))
    pyautogui.press("enter")
