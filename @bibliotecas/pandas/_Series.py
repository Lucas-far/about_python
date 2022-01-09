

from pandas import Series

_ = '------------------------------------------------------------------------------------------------------------------'
x = '\n'
dict_ = {
    'nome': 'Lucas',
    'sobrenome': 'Farias',
    'complemento': 'Santos de Sousa'
}
str_ = 'Lucas Farias Santos de Sousa'
tuple_ = ('Lucas', 'masculino', 'Brasil')

object_1 = Series(data=5)                 # Objeto Series inteiro
object_2 = Series(data=0.5)              # Objeto Series flutuante
object_3 = Series(data=str_)             # Objeto Series string
object_4 = Series(data=str_.split(' '))  # Objeto Series lista
object_5 = Series(data=tuple_)           # Objeto Series tupla
object_6 = Series(data=dict_)            # Objeto Series dicionário

print((1, 'int'), _)
print(object_1, x)
print((2, 'float'), _)
print(object_2, x)
print((3, 'str'), _)
print(object_3, x)
print((4, 'list'), _)
print(object_4, x)
print((5, 'tuple'), _)
print(object_5, x)
print((6, 'dict'), _)
print(object_6, x)
