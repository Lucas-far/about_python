

"""
Objetivo
    clicar, segurar e mover, a partir de uma coordenada x e y, para outra coordenada, informada nos parâmetros

Observações
    1. o parâmetro especifica a quantidade de pixels que o mouse será movido
    2. não é recomendável usar coordenadas x e y juntas, ou seja: drag(x, 0) ou drag(0, y)
    3. caso usem-se x e y juntos, é recomendável usar o menor valor possível (ver exemplo abaixo)
    4.
"""

from pyautogui import drag

"Form básica"
# drag(qtd. pixels em x, qtd. pixels em y, intervalo)
drag(500, 0, 2)

def algoritmo_desenhar_letra():
    contador = 0
    contador2 = 0

    # Tracejar da esquerda para a direita
    while contador <= 9:
        drag(1, 1)
        drag(0, 1)
        contador += 1

    # Tracejar da direita para a esquerda
    while contador2 <= 9:
        drag(1, -1)
        drag(0, -1)
        contador2 += 1
