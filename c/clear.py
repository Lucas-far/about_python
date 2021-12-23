

"""
Objetivo:
    esvaziar dados de classes iteráveis específicas
"""

# @dict @list @set

def scan(classe, dado):
    try:
        var = dado
        var.clear()
        print(classe, var)
    except AttributeError as error2:
        print('{}{}{}'.format('\033[1:31m', error2, '\033[m'))

scan('booleano', True)
scan('complexo', 7j)
scan('dicionário', {7: 7})
scan('flutuante', 7.0)
scan('inteiro', 7)
scan('lista', [7])
scan('nenhum', None)
scan('range', range(1, 4))
scan('conjunto', {7})
scan('string', 'pyt')
scan('tupla', (7,))
