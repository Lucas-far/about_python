
"""
Objetivo:
     adicionar um dado iterável em uma classe deque, no índice 0

Observação:
    1. apenas classes iteráveis podem ser adicionadas com esse método
    2. aceita apenas um argumento por uso, e o iterável passado, conta como apenas um índice
    3. pode ser usado multiplamente em linha
"""

from collections import deque

def scan(classe, dado, valor):
    try:
        var = dado
        var.extendleft(valor)
        print(classe, var)
    except AttributeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True, False)
scan('complexo', 7j, '3j')
scan('dicionário', {}, {'c': 'v'})
scan('flutuante', 7.0, '3.0')
scan('inteiro', 7, '3')
scan('lista', [], 'l')
scan('nenhum', None, None)
scan('range', range(1, 4), range(5, 6))
scan('conjunto', {'cj'}, '7')
scan('string', 'str', 'ing')
scan('tupla', (), ('t',))
scan('deque', deque([]), 'dq')

"Em linha"
dq = deque(['l'])
dq.extendleft('i'), dq.extendleft('s')
print(1, dq)

"Em quebra de linha"
dq.extendleft('t')
dq.extendleft('a')
print(2, dq)
