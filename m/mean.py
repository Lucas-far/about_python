

"""
Objetivo:
     retornar a média entre classes inteiras e/ou flutuantes, misturadas ou separadas, dentro de um iterável
"""

# @dict @list @range @set @tuple

from statistics import mean

def scan(classe, dado):
    try:
        print(classe, mean(dado))
    except TypeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True)
scan('complexo', 7j)
scan('dicionário', {2.7: 2.7, 7.2: 7.2})
scan('flutuante', 7.0)
scan('inteiro', 7)
scan('lista', [3, 7, 11.2])
scan('nenhum', None)
scan('range', range(1, 4))
scan('conjunto', {14, 9.7})
scan('string', '22')
scan('tupla', (10, 7))

print([1], mean((5, 10, 15, 20, 25, 30)))             # exemplo 1 (tupla)
print([2], cj := mean({99, 16.4, 7.75, 86.1, 51.6}))  # exemplo 2 (conjunto)
