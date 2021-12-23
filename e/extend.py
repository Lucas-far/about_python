

"""
Objetivo:
    adicionar um dado em uma classe iterável lista

Observação:
    1. apenas classes iteráveis podem ser adicionadas com esse método
    2. aceita apenas um argumento por uso, e o iterável passado, conta como apenas um índice
    3. pode ser usado multiplamente em linha
"""

def scan(classe, dado, valor):
    try:
        var = dado
        var.extend(valor)
        print(classe, var)
    except AttributeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True, False)
scan('complexo', 7j, '3j')
scan('dicionário', {}, {'c': 'v'})
scan('flutuante', 7.0, '3.0')
scan('inteiro', 7, '3')
scan('lista', [], 'l')
scan('nenhum', None, None)
scan('range', range(1, 4), range(5, 6))
scan('conjunto', {'cj'}, '7')
scan('string', 'str', 'ing')
scan('tupla', (), ('t',))

"Em linha"
li = ['l']
li.extend('i'), li.extend('s')
print(1, li)

"Em quebra de linha"
li.extend('t')
li.extend('a')
print(2, li)
