

"""
Curiosidade? Converter inteiros em lista para string com valores pontuados
"""

value = ''
list_ = [2, 8, 9, 2, 4, 5, 8]

print(list_)                          # [2, 8, 9, 2, 4, 5, 8]
list_.insert(1, '.')
print(list_)                          # [2, '.', 8, 9, 2, 4, 5, 8]
list_.insert(5, '.')
print(list_)                          # [2, '.', 8, 9, 2, '.', 4, 5, 8]

value_as_string = "".join([str(number) for number in list_])
print([1], value_as_string)
