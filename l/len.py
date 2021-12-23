

"""
Objetivo:
     retornar a quantidade de dados/índices que uma classe iterável contêm
"""

# @dict @list @range @set @str @tuple

def scan(classe, dado):
    try:
        print(classe, len(dado))
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

print([1], len({False, None, True, 0.1, 2.0}))                 # exemplo 1
print([2], v := len(['l', {'i'}, ['s'], ('t',), {'a': 'a'}]))  # exemplo 2

# Estranhezas relacionadas ao método e a classe conjunto
print(len({False, 0}))  # aqui deveria ser 2, mas é 1, pois False = 0, e em conjunto dados repetidos não contam
print(len({True, 1}))   # idem......................., pois True = 1, e em conjunto dados repetidos não contam
print(len({1, 1.0}))    # idem......................., pois float int = int, e em conjunto dados repetidos não contam
