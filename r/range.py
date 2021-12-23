

"""
Objetivo:
    gerar sequências numéricas inteiras para ser usada em classes iteráveis, loops
"""

# Range com sintaxe normal
print([1], f"{list(range(8)) = }")
print([2], f"{list(range(1, 8)) = }")   # par 2 (não inclusivo)
print([3], f"{list(range(1, 8, 2)) = }")

# Range com sintaxe negativa
print([4], f"{list(range(-7, 0)) = }")  # par 2 (não inclusivo)
print([5], f"{list(range(-7, 0, 2)) = }")

# Em loop
for each_data in range(1, 8):
    print(each_data)

for index, each_data in enumerate([13, 19, 10, 12, 7]):
    if each_data in range(1, 10):
        print('Sim, está no índice', index)
        break
