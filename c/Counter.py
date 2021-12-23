

"""
Objetivo:
    gerar um dicionário da quantidade de vezes que cada um dos dados em uma classe iterável, repete-se
"""

from collections import Counter

# @dict @list @range @set @str @tuple

def obs():
    """
    @dict  -> funciona, mas somente se sob influência de métodos .keys() .values()
    @none  -> funciona, mas não gera retorno
    @range -> funciona, mas só é útil quando está dentro de um iterável, e em + de 1
    @set   -> funciona, mas é inútil, pois classe conjunto não repete dados
    """

def scan(classe, dado):
    try:
        print(classe, Counter(dado))
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
scan('tupla', ('a', 'b', 'c', 'a'))
