

"""
Objetivo:
    verificar se dados são compatíveis, idênticos, ou se um ou mais dados encontram-se dentro de outro dado
"""

# Tipos de operadores lógicos e suas variações
print([1], False)      # falso padrão
print([2], not True)   # falso alternativo
print([3], True)       # verdadeiro padrão
print([4], not False)  # verdadeiro alternativo

# Combinando operadores lógicos com de comparação
print([5], f'{True < True = }')
print([6], f'{True <= False = }')
print([7], f'{not True > False = }')
print([8], f'{True >= False = }')
print([9], f'{True is not False = }')
print([10], f'{True is False = }')

# Usando operadores lógicos de forma contextual
print([11], f'{(0.7 < 0.77) = }')
print([12], f'{({"a": "b"} == {"a": "b"}) = }')
print([13], f'{([""] != [" "]) = }')
