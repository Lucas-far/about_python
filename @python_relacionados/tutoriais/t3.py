

"""
Objetivo
    fazer cálculos sequências, nesse contexto, calcular a mudança do preço de um produto em cada parcela
"""
# todo Tutorial 3

valor = 232.17
parcelas = \
    """
    ======= Parcelamento =======
    Preço do produto: {}
    2 parcelas: {:.2f}
    3 parcelas: {:.2f}
    4 parcelas: {:.2f}
    5 parcelas: {:.2f}
    6 parcelas: {:.2f}
    7 parcelas: {:.2f}
    8 parcelas: {:.2f}
    9 parcelas: {:.2f}
    """

# Se no contexto, há 9 parcelas, então range(2, 10) = 2 até 9
resultado = [valor / parcela for parcela in range(2, 10)]
print(resultado)
# [116.085, 77.39, 58.0425, 46.434, 38.695, 33.167142857142856, 29.02125, 25.796666666666667]
print(parcelas.format(valor, *resultado))
