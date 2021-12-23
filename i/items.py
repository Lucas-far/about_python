

"""
Objetivo:
     mostrar os elementos de uma classe dicionário: chave e valor, em forma de tupla

Observação:
    1. dicionários sob a influência do método, tornam-se incapazes de chamar chave
        1.1 para corrigir esse comportamento, o dicionário precisa receber cast (ver def detalhes)
"""

# @dict

def scan(classe, dado):
    try:
        print(classe, dado.items())
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

# Diferença: dicionário comum vs dicionário .items()
print([1], {'a': 1, 'b': 2, 'c': 3})
print([2], {'a': 1, 'b': 2, 'c': 3}.items())

# Um dicionário comum consegue acessar a chave
print([3], d := {'a': 1, 'b': 2, 'c': 3})
print([4], d['a'])

# Ao usar: .keys() ou .items() ou .values(), perde-se o acesso por chave
try:
    print(d['a'])
except TypeError as error2:
    print('\033[1:32m' + str(error2) + '\033[m')

# O novo acesso acontece através por cast
print([3], list(d)[0])
print([4], list(d).pop(list(d).index('a')))

# Formas diferentes de mostar dados em iteração de dicionário
d = {'a': 1, 'b': 2}

for key, value in d.items():      # não gera-se tupla
    print(key, value)

for each_key_value in d.items():  # gera-se tupla
    print(each_key_value)
