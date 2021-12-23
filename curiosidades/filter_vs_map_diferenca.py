

var = list(range(1, 11))
print(list(map(lambda def_: not def_ % 2, var)))     # transforma dados
print(list(filter(lambda def_: not def_ % 2, var)))  # filtra dados

var2 = ['dado1', 'dado2', 'dado3', '...']
print(list(map(lambda x: 'dado' in x, var2)))     # transforma dados
print(list(filter(lambda x: 'dado' in x, var2)))  # filtra dados
