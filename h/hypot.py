

"""
Objetivo:
    calcular hipotenusa

Observação:
    1. dados iteráveis podem ser usados com o método, se forem descompactados
    2. a lógica do método recebe 2 parâmetros, mas não gera erro se mais de 2 forem adicionados
"""

from math import hypot

# @bool @float @int

def scan(classe, v1, v2):
    try:
        print(classe, hypot(v1, v2))
    except TypeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True, True)
scan('complexo', 7j, 3j)
scan('dicionário', {'c': 'v'}, {'C: V'})
scan('flutuante', 7.0, 11.0)
scan('inteiro', 7, 3)
scan('lista', ['l'], ['L'])
scan('nenhum', None, None)
scan('range', range(7), range(11))
scan('conjunto', {'cj'}, {'CJ'})
scan('string', 's', 'S')
scan('tupla', ('t',), ('T',))

# usando o método com iteráveis descompactados
print([1], hypot(*{10.7, 20}))
print([2], hypot(*[10.7, 20]))
print([3], hypot(*(10.7, 20)))
