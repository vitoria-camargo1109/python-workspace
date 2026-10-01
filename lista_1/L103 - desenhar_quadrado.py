# Abra o Paint e use moveTo() e dragTo() para desenhar um quadrado na tela.

import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("paint")
pyautogui.press("enter")

time.sleep(1)
pyautogui.moveTo(713, 429)
pyautogui.dragTo(713, 869, duration=0.3)

pyautogui.moveTo(713, 869)
pyautogui.dragTo(1177, 869, duration=0.3)

pyautogui.moveTo(1177, 869)
pyautogui.dragTo(1177, 429, duration=0.3)

pyautogui.moveTo(1177, 429)
pyautogui.dragTo(713, 429, duration=0.3)
