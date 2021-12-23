

"""
Objetivo:
    retornar [ True ou False ] para se um dado encontra-se dentro de uma classe iterável
    o método [ .__contains__() ] é similar a palavra reservada Python [ in ]
"""

# @dict @list @range @set @str @tuple

def scan(classe, dado, valor):
    try:
        print(classe, dado.__contains__(valor))
    except AttributeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True, True)
scan('complexo', 7j, 3j)
scan('dicionário', {1: 2}, 1)  # se contêm chave = 1
scan('flutuante', 7.0, 7)
scan('inteiro', 7, 7.0)
scan('lista', [-7, '...'], ['...'])
scan('nenhum', None, None)
scan('range', range(-7, -6), -7)
scan('conjunto', {-7}, None)
scan('string', '...', '.')
scan('tupla', (-7,), (-7))

# Similaridade de [ .__contains__() ] com [ in ]
print(1, t2 := ('Brasil', 'America do Sul', 'Hemisfério Norte').__contains__('Brasil'))
print(2, t3 := 'Brasil' in ('Brasil', 'America do Sul', 'Hemisfério Norte'))
