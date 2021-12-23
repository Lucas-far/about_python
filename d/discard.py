

"""
Objetivo
     excluir um dado específico de uma classe conjunto

Observação
    1. se o dado a ser excluido não existir no conjunto, não retorna-se erro
    2. pode ser usado multiplamente em linha
"""

# @set

def scan(classe, dado, valor):
    try:
        var = dado
        var.discard(valor)
        print(classe, var)
    except AttributeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True, True)
scan('complexo', 7j, 7j)
scan('dicionário', {'c': 'v'}, {'c'})
scan('flutuante', 7.0, 7.0)
scan('inteiro', 7, 7)
scan('lista', ['list'], 'list')
scan('nenhum', None, None)
scan('range', range(1, 4), 1)
scan('conjunto', {'set'}, 'set')
scan('string', 'str', 'r')
scan('tupla', ('tuple',), 'tuple')
