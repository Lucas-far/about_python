

"""
Objetivo:
    retornar a posição de um objeto na tela

Observação:
    1. para saber a posição de um objeto na tela, a IDE precisa estar minimizada, parcialmente
    2. mesmo minimizado, mantenha o cursos selecionado na tela da IDE
    3. direciona-se o mouse para o abjeto na tela, sem clicar nele, pois a IDE deve estar selecionada
    4. quando estiver na posição, faça: [ shift + ctrl + fn + f10 ]
"""

from pyautogui import position

print([1], position())
print([2], coord := position())
