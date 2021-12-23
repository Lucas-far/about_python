

"""
Objetivo:
    anexar qualquer tipo de classe à uma variável de classe lista

Observação:
    1. pode ser usado multiplamente em linha (separação por vírgula)
    2. dados iteráveis com + de 1 índice, quando adicionados por esse método, contam apenas como 1 índice
"""

# @list

def scan(classe, dado, valor):
    try:
        var = dado
        var.append(valor)
        print(classe, var)
    except AttributeError as error2:
        print('{}{}{}'.format('\033[1:31m', error2, '\033[m'))

scan('booleano', True, False)
scan('complexo', 7j, 3j)
scan('dicionário', {}, {-7: -7})
scan('flutuante', 7.0, -7.0)
scan('inteiro', 7, -7)
scan('lista', [], ())
scan('nenhum', None, 0)
scan('range', range(1, 4), range(5, 6))
scan('conjunto', {3}, 7)
scan('string', 'pyt', 'hon')
scan('tupla', (), (0,))

"Em linha"
print(12, l2 := [])  # []
l2.append(False), l2.append(None), l2.append(True)
print(12, l2)        # [False, None, True]

"Tradicional"
print(13, l3 := [])  # []
l3.append(0)
l3.append(1.0)
l3.append('str')
print(13, l3)        # [0, 1.0, 'str']
