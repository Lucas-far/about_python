

"""
Objetivo:
    retornar dado em iterável lista que mais ocorre dentro dela

Observação:
    1. pode ser usada em classe conjunto e dicionário, mas é irrelevante, pois ambas não permitem repetição de dados
"""

# @dict @list @range @set @str @tuple

from statistics import multimode

def scan(classe, dado):
    try:
        print(classe, multimode(dado))
    except TypeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True)
scan('complexo', 7j)
scan('dicionário', {'c': 'v', 'c2': 'v2'})
scan('flutuante', 7.0)
scan('inteiro', 7)
scan('lista', ['l', 'i', 's', 't', 'a', 'l'])
scan('nenhum', None)
scan('range', range(1, 4))
scan('conjunto', {'s', 'e', 't'})
scan('string', 'strings')
scan('tupla', ('t', 'u', 'p', 'l', 'a', 't'))

print([1], multimode(['a', 'b', 'c', None, None, None]))
# Caso não haja dados reincidentes ou reincidentes iguais, todos são retornados
print([2], t := multimode(('a', 'b', 'c', None, True, False)))
