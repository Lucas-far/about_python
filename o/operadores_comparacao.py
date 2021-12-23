

"""
Objetivo:
    comparar dados de classe numérica, gerando um booleano dessa comparação
"""

from datetime import datetime

# OBS: o sinal de igual ao final não faz parte da sintaxe dos operadores, mas a fstring f""
print([1], f'{10 < 20 = }')
print([2], f'{10 <= 20 = }')  # operador de dupla função, se uma das funções satisfazer, o retorno: True
print([3], f'{10 > 20 = }')
print([4], f'{10 >= 20 = }')  # operador de dupla função, se uma das funções satisfazer, o retorno: True
print([5], f'{10 == 20 = }')
print([6], f'{10 != 20 = }')

# Usando operadores de comparação (testando todas as horas possíveis por variável + loop while)
def ex():
    hora = 0
    while hora <= 23:
        if 0 <= hora <= 11:
            print(hora, 'Bom dia')
            hora += 1
        elif 12 <= hora <= 17:
            print(hora, 'Boa tarde')
            hora += 1
        elif 18 <= hora <= 23:
            print(hora, 'Boa noite')
            hora += 1
    del hora

# Usando operadores de comparação (testando todas as horas possíveis por variável datetime + condições)
def ex2():
    tempo = (datetime.today().hour, datetime.today().minute, datetime.today().second)
    if 0 <= tempo[0] <= 11:
        print(tempo[0], 'Bom dia')
    elif 12 <= tempo[0] <= 17:
        print(tempo[0], 'Boa tarde')
    elif 18 <= tempo[0] <= 23:
        print(tempo[0], 'Boa noite')
    del tempo

# Testando todas as horas possíveis por (iterável + loop for)
def ex3():
    hora = [*range(0, 24)]
    for h in hora:
        if h in hora[0:12]:
            print(h, 'Bom dia')
        elif h in hora[12:18]:
            print(h, 'Boa tarde')
        elif h in hora[18:]:
            print(h, 'Boa noite')
    del hora

ex(), ex2(), ex3()
