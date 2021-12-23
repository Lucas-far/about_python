

"""
Objetivo:
    converter uma classe iterável que contenham apenas dados de string nela, para uma classe string

Observação:
    1. método que contêm string em sua sintaxe, para adicionar caracteres separadores entre cada letra, se desejado
"""

# @dict @list @set @str @tuple

def scan(classe, dado):
    try:
        print(classe, "".join(dado))
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

print([1], "".join(('t', 'u', 'p', 'l', 'a')))  # exemplo 1 (tupla)
print([2], cj := "".join({'s', 'e', 't'}))      # exemplo 2 (conjunto)
