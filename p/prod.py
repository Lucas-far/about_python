

"""
Objetivo:
    multiplicar em uma classe iterável ou livre/solto, o resultado de dados numéricos

Observação:
    1. o método têm uma lógica similar ao método: [ mean() ] da biblioteca statistics
    2. seu uso funciona com iteráveis, contanto que os dados nela sejam todos numéricos
    3. em caso de dados complexos dentro de iteráveis, a IDE reclama, mas não gera-se erro
    4. em caso de iterável range, este precisa estar desempacotado dentro de outro iterável
"""

# @dict @list @range @set @tuple

from statistics import mean
from math import prod

def scan(classe, dado):
    try:
        var = dado
        print(classe, prod(var))
    except TypeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True)
scan('complexo', 7j)
scan('dicionário', {10: 100, 20: 200})
scan('flutuante', 7.0)
scan('inteiro', 7)
scan('lista', [9, 9])
scan('nenhum', None)
scan('range', range(1, 4))
scan('conjunto', {9, 8})
scan('string', '97')
scan('tupla', (9, 6))

# Similaridade de lógica, obviamente não é a mesma coisa
print([1], 'MÉTODO mean =', mean([1, 2, 3, 4, 5]))
print([2], 'MÉTODO prod =', prod([1, 2, 3, 4, 5]))
print([3], prod([7, 7]))                 # literal
print([4], cj := prod({*range(7, 11)}))  # em variável
