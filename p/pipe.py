

"""
Objetivo:
    unir dados des conjuntos em um só

Observação:
    1. método é a versão resumida do método .union()
"""

# @set

def scan(classe, dado, dado2):
    try:
        print(classe, dado | dado2)
    except TypeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True, {False})
scan('complexo', 7j, {'7j'})
scan('dicionário', {'c': 'v'}, {'C'})
scan('flutuante', 7.0, {'7.0'})
scan('inteiro', 7, {'7'})
scan('lista', ['l'], {'L'})
scan('nenhum', None, {'N'})
scan('range', range(1, 4), {'R'})
scan('conjunto', {'cj'}, {'CJ'})
scan('string', 's', {'S'})
scan('tupla', ('t',), {'T'})

print([1], {1, 2, 3} | {1.1, 2.2, 3.3} | {1.1j, 2.2j, 3.3j})  # Três conjunto tornam-se um
print([2], cj := {'a'} | {'b'} | {'c'})                       # Três conjunto tornam-se um
