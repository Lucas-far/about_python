

"""
Objetivo
    retornar os dados diferentes de uma variável conjunto, em relação à outras variáveis conjunto
"""

# @set

cj, cj2, cj3 = {0}, {0, 1}, {0, 1, 2}
resultado = {0, 1, 2, 3}.difference(cj, cj2, cj3)
print(1, resultado)

# Mecânica
"O conjunto matriz recebe o método .difference()"     # resultado = {0, 1, 2, 3}.difference()
"O conjunto alvo vai dentro do método .difference()"  # .difference(cj, cj2, cj3)
"Se há, no conjunto matriz, algum dado que não esteja em NENHUM dos conjuntos alvo, esse será o retorno do método"
