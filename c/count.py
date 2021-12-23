

"""
Objetivo:
    retornar a classe inteiro de quantas vezes um dado dentro de uma classe iterável, repetiu-se
"""

# @list @range @str @tuple

def scan(classe, dado, par):
    try:
        print(classe, dado.count(par))
    except AttributeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True, 'u')
scan('complexo', 0j, 'u')
scan('dicionário', {'_': '__'}, 'u')
scan('flutuante', 0.0, 'u')
scan('inteiro', 0, 'u')
scan('lista', [x for x in 'Albuquerque'], 'u')
scan('nenhum', None, 'u')
scan('range', range(1, 11), 10)
scan('conjunto', {'_'}, 'u')
scan('string', 'Albuquerque', 'q')
scan('tupla', ('a', 'a', 'a'), 'a')
