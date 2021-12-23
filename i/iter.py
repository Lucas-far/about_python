

"""
Objetivo:
    tornar uma variável iterável capaz de chamar dados de forma singular, sem usar indexação

Observação:
    1. O método torna a variável percorrível singularmente, mas depende de outro método: next()
    2. Se o método next() não for usado junto, mostra-se apenas um objeto de memória
    3. Se for tentado usar indexação, gera-se TypeError
    4. Funciona em dicionário, mas é desnecessário
    5. Funciona em conjunto, mas a iteração é aleatória, portanto, não será controlada
    6. Para não exibir um dado, usa-se next() fora de um print, e para exibir, faz-se o inverso (ver def var_nova)
"""

# @dict @list @range @set @str @tuple

def scan(classe, dado):
    try:
        print(classe, iter(dado))
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

# Usando iter() -> a cada next() fora de um print(), um dado é percorrido sem ser exibido
print([1], s := iter('Python')), next(s), next(s), print(next(s)), print(next(s))
