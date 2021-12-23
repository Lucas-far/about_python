

"""
Objetivo:
     mostrar todas e somente as chaves contidas em uma classe dicionário

Observação:
    1. dicionários sob a influência do método, tornam-se incapazes de chamar chave
        1.1 para corrigir esse comportamento, o dicionário precisa receber cast iterável (ver def detalhes)
"""

# @dict

def scan(classe, dado):
    try:
        print(classe, dado.keys())
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

print([1], {1: [1], 2: {2}, 3: (3,)}.keys())         # exemplo 1
print([2], d := {'1': 1, '2': 2.0, '3': 3j}.keys())  # exemplo 2

# Ao usar: .keys() ou .items() ou .values(), perde-se o acesso por chave
try:
    print(d['1'])
except TypeError as error:
    print('\033[1:32m' + str(error) + '\033[m')

# O novo acesso acontece através por cast
print([3], list(d)[1])
print([4], list(d).pop(list(d).index('2')))
