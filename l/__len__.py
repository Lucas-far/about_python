

"""
Objetivo:
     retornar a quantidade de dados/índices que uma classe iterável contêm

Observação:
    1. não funciona com classes não iteráveis
"""

# @dict @list @range @set @str @tuple

def scan(classe, dado):
    try:
        print(classe, dado.__len__())
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
