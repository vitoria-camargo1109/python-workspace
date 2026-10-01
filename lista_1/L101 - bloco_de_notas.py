# Abrir o Bloco de Notas e escrever um texto. Salve com hotkey("ctrl", "s").


import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("bloco de notas")
pyautogui.press("enter")

time.sleep(2)
pyautogui.write("Bem-vindo!")
pyautogui.hotkey("ctrl, s")
