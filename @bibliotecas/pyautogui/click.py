

"""
Objetivo:
    mover o ponteiro do mouse para uma coordenada da tela especificada

Observação:
   somente os 2 primeiros args do método são mandatórios
"""

from pyautogui import click

# click(x, y, qtd. cliques, intervalo, botão)
click(500, -200, 2, 1, button='left')
click(500, -200, 2, 1, button='right')
