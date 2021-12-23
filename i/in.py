

"""
Objetivo:
    palavra reservada para realizar loop for

Objetivo 2:
    checar se um dado é pertencente a um outro dado, gerando um booleano

Observação
    1. A sintaxe funciona somente com classes iteráveis
"""

# @list @range @str @tuple

def scan(classe, dado, var):
    try:
        print(classe, dado in var)
    except TypeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True, False)
scan('complexo', 7j, 10j)
scan('dicionário', {'c': 'v'}, {'c': 'v'})
scan('flutuante', 7.0, 5.0)
scan('inteiro', 7, 2)
scan('lista', ['l'], ['l'])
scan('nenhum', None, None)
scan('range', range(1, 4), range(1, 11))
scan('conjunto', {'cj'}, {})
scan('string', 's', 's')
scan('tupla', ('t',), ('T',))

# Uso em loop for
print([1], [x.replace(x, '*') for x in 'Albuquerque'])
print([2], [x.upper().split() if x == 'u' else x for x in 'Albuquerque'])
print([3], [{x} for x in enumerate('ok')])

# Uso comum
print([4], [] in ['l'])             # lista
print([5], 7 in range(1, 11))       # range
print([6], '_' in '_()')            # string
print([7], 'a' in ('a', 'b', 'c'))  # tupla
