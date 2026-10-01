"""
Crie um script que imprima pyautogui.position() a cada segundo 
durante 10 segundos, para treinar a captura de posições na tela.
"""

import pyautogui
import time

for segundo in range(10):
    posicao = pyautogui.position()
    print(posicao)
    time.sleep(1)