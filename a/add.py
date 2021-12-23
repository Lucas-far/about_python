

"""
Objetivo:
     anexar um novo dado à uma variável de classe conjunto

Observação:
    1. pode ser usado multiplamente em linha, se separado por vírgula
    2. o método aceita somente um parâmetro por uso
    3. classe conjunto é intolerante às classes: conjunto, dicionário e lista
"""

# @set

def scan(classe, dado, valor):
    try:
        var = dado
        var.add(valor)
        print(classe, var)
    except AttributeError as error2:
        print('{}{}{}'.format('\033[1:31m', error2, '\033[m'))

scan('booleano', True, False)
scan('complexo', 7j, 3j)
scan('dicionário', {}, {-7: -7})
scan('flutuante', 7.0, -7.0)
scan('inteiro', 7, -7)
scan('lista', [], [-7])
scan('nenhum', None, 0)
scan('range', range(1, 4), range(5, 6))
scan('conjunto', {3}, 7)
scan('string', 'pyt', 'hon')
scan('tupla', (), (0,))

"Em linha"
print(1, cj2 := set({}))  # set()
cj2.add(False), cj2.add(None), cj2.add(True)
print(1, cj2)             # {False, True, None}

"Tradicional"
print(2, cj3 := set({}))  # set()
cj3.add(0)
cj3.add(1.0)
cj3.add('str')
print(2, cj3)             # {0, 1.0, 'str'}
