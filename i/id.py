

"""
Objetivo:
    criar um identificador inteiro para qualquer tipo de classe, literal ou em variável
"""

def scan(classe, dado):
    try:
        print(classe, id(dado))
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

print([1], id(False))
print([2], cj := id({'str'}))

# Mesmo sendo iguais, variáveis nunca criam ids idênticos
l = []
l2 = []
print([3], id(l) == id(l2))
