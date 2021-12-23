

"""
Objetivo:
    escolher um dos dados dentro de uma classe iterável
"""

from random import choice

# @list @range @str @tuple

def scan(classe, dado):
    try:
        print(classe, choice(dado))
    except TypeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True)
scan('complexo', 0j)
scan('dicionário', {'a': 'b', 'y': 'z'}.keys())
scan('flutuante', 0.0)
scan('inteiro', 0)
scan('lista', [x for x in 'Albuquerque'])
scan('nenhum', None)
scan('range', range(1, 11))
scan('conjunto', {'.', '.', '.'})
scan('string', 'Augusto')
scan('tupla', ('a', 'b', 'c', 'd', 'e'))
