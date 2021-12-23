

"""
Objetivo:
    retornar inteiro da quantidade de bytes em memória armazenados em um var ou dado literal
"""

from sys import getsizeof as _

def scan(classe, dado):
    try:
        print(classe, _(dado), 'bytes')
    except AttributeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True)
scan('complexo', 7j)
scan('dicionário', {'c': 'v'})
scan('flutuante', 7.0)
scan('inteiro', 7)
scan('lista', ['l'])
scan('nenhum', None)
scan('range', range(1, 4))
scan('conjunto', {'cj'})
scan('string', 's')
scan('tupla', ('t',))
