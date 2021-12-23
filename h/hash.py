

"""
Instalação:
    pip install passlib

Objetivo:
    criptografar dados, mudando seus dados visuais originais

Observação:
    1. a importação do método é complexa, portanto recomenda-se um apelido
"""

from passlib.hash import pbkdf2_sha256 as codify

# @str

def scan(classe, dado):
    try:
        print(classe, codify.hash(dado))
    except TypeError as error:
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

# TODO -> Apesar de funcionar somente em string, também pode ser usado em iterável, caso haja somente strings nela
print([1], [codify.hash(x) for x in {'python', 'django', 'pycharm'}])
print([2], codify.hash(('abcdefghijklmnopqrstuvwxyz',)[0]))
