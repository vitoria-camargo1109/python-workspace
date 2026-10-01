"""
Use pyautogui.screenshot() para tirar uma captura de tela e salve a imagem com 
a data e a hora no nome do arquivo.
"""

import pyautogui

from datetime import datetime
agora = datetime.now().strftime("%d-%m-%Y, %H-%M")
pyautogui.screenshot(f"captura{agora}.png")
