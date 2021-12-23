

"""
Objetivo:
    remover a última chave e seu valor de um dicionário
"""

# @dict

def scan(classe, dado):
    try:
        var = dado
        print(classe, var.popitem())
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

print([1], {'c': 'v', 'c2': 'v2', 'c3': 'v3'}.popitem())
print([2], d := {'c': 'v', 'c3': 'v3', 'c2': 'v2'}.popitem())

def acessar():
    """
    python / dir({})

    '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
    '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__',
    '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__',
    '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys',
    'pop', 'popitem', 'setdefault', 'update', 'values'
    """
