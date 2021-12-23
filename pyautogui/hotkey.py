

"""
Objetivo:
    executar uma chave do teclado específica ou combinada

Observação:
    1. Não sei se há comandos com 4 teclas que possam ser tentados com esse método
    2. O método aceita um comando por uso, dois comandos por uso, pode gerar conflitos na execução
"""

from pyautogui import hotkey

hotkey('enter')              # Entrada única
hotkey('win', 'd')           # Entradas combinadas [ exibição do desktop no Windows ]
hotkey('alt', 'space', 'x')  # Entradas combinadas [ maximização de janelas no Windows e navegadores ]
