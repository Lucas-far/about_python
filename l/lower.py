

"""
Objetivo:
     converter todos os caracteres de uma classe string para cacha baixa

Observação:
    1. uso em classe string ou classe iterável somente com dado strings nela, exceto conjunto, por não aceitar indexação
"""

# @str

def scan(classe, dado):
    try:
        print(classe, dado.lower())
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

print([1], 'ALFREDO'.lower())                                        # exemplo 1
print([2], l := ['UTOPIA'][0].lower())                               # exemplo 2
print([3], " ".join([x.lower() for x in ('PAI', 'FILHO', 'NETO')]))  # exemplo 3
