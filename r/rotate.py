

"""
Objetivo:
    deslocar dados de deque de um lado para o outro, selecionando-os por quantidade

Observação:
    1. o inteiro passado como parâmetro do método, é igual ao número de índices deslocados
    2. se o inteiro for positivo, por exemplo, 5: desloca-se os 5 últimos índices, para o início do deque
    3. se o inteiro for negativo, por exemplo, -5: desloca-se os 5 primeiros índices, para o fim do deque
"""

from collections import deque

# @deque

def scan(classe, dado):
    try:
        var = dado
        dado.rotate(2)
        print(classe, var)
    except AttributeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True)
scan('complexo', 7j)
scan('dicionário', {'c': 'v', 'c2': 'v2'})
scan('flutuante', 7.0)
scan('inteiro', 7)
scan('lista', ['l', 'L'])
scan('nenhum', None)
scan('range', range(1, 4))
scan('conjunto', {'cj', 'CJ'})
scan('string', 'sS')
scan('tupla', ('t', 'T'))
scan('deque', deque(['d', 'e', 'q', 'u', 'e']))

print([1], dq := deque([*range(1, 14)])), dq.rotate(-5), print([2], dq)
print([3], dq2 := deque([*range(1, 14)])), dq2.rotate(5), print([4], dq2)

def acesso():
    """
    python / from collections import deque / dir(deque([]))

    '__add__', '__bool__', '__class__', '__contains__', '__copy__', '__delattr__', '__delitem__', '__dir__', '__doc__',
    '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__',
    '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
    '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
    '__str__', '__subclasshook__', 'append', 'appendleft', 'clear', 'copy', 'count', 'extend', 'extendleft', 'index',
    'insert', 'maxlen', 'pop', 'popleft', 'remove', 'reverse', 'rotate'
    """
