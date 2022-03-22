

from os import chdir, getcwd, listdir, mkdir
import pyautogui
from keyboard import is_pressed
from time import sleep
# from os import getcwd, listdir, mkdir

chdir('c:\\users\\lucasf\\desktop\\teste')

index = 1
while True:
    # 1 = distância da esquerda
    # 2 = distância do topo
    # 3 = largura
    # 4 = altura
    pyautogui.screenshot(f'arquivo{index}.png',
                         region=(1107, 545, 106, 155))
    index += 1

    if is_pressed('q'):
        exit(0)
