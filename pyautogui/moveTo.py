

"""
Objetivo:
    mover (não clicar ou segurar) o ponteiro do mouse, a partir de uma coordenada inicial, para outra

Observação:
    [ par 1 & par 2 ] = as coordenadas podem ser valores negativos ou positivos (cima, direita, baixo, esquerda)
    [ par 3 ]         = intervalos entre as ações, sendo opcional
"""

from pyautogui import hotkey, moveTo

def fazer_cruz_desktop():
    var = [
        hotkey('win', 'd'), moveTo(500, 500, 0.5), moveTo(500, 400, 0.5), moveTo(500, 500, 0.5), moveTo(600, 500, 0.5),
        moveTo(500, 500, 0.5), moveTo(500, 600, 0.5), moveTo(500, 500, 0.5), moveTo(400, 500, 0.5), moveTo(500, 500, 0.5)
    ]
    print(var)

fazer_cruz_desktop()
