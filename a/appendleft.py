

"""
Objetivo:
    anexar qualquer tipo de classe à uma variável de classe deque/lista, a partir do índice 0 (sempre)

Observação:
    1. a classe [ deque ] têm a mesma biblioteca de métodos da classe [ lista ], mas com métodos adicionais
    2. pode ser usado multiplamente em linha (separação por vírgula)
    3. dados iteráveis com + de 1 índice, quando adicionados por esse método, contam apenas como 1 índice
"""

from collections import deque

# @deque

def scan(classe, dado, valor):
    try:
        var = dado
        var.appendleft(valor)
        print(classe, var)
    except AttributeError as error2:
        print('{}{}{}'.format('\033[1:31m', error2, '\033[m'))

scan('booleano', True, False)
scan('complexo', 7j, 3j)
scan('dicionário', {}, {-7: -7})
scan('flutuante', 7.0, -7.0)
scan('inteiro', 7, -7)
scan('lista', [], ())
scan('nenhum', None, 0)
scan('range', range(1, 4), range(5, 6))
scan('conjunto', {3}, 7)
scan('string', 'pyt', 'hon')
scan('tupla', (), (0,))
scan('deque', deque([]), '...')

"Em linha"
print(1, d := deque([]))  # deque([])
d.appendleft(False), d.appendleft(None), d.appendleft(True)
print(1, d)               # deque([True, None, False])

"Tradicional"
print(2, de := deque([]))  # deque([])
de.appendleft(0)
de.appendleft(1.0)
de.appendleft('str')
print(2, de)               # deque(['str', 1.0, 0])
