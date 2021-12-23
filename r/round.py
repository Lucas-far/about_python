

valor_1 = 0.7
print([1], valor_1)

valor_1 = round(valor_1)  # se a parte decimal estiver mais perto do valor seguinte, o valor decimal torna-se ele
print([2], valor_1)

valor_1 = 0.5
valor_1 = round(valor_1)  # se a parte decimal estiver mais perto do valor anterior, o valor decimal torna-se ele
print([3], valor_1)

valor_1 = 0.5777
valor_1 = round(valor_1, 2)  # se o valor decimal for grande, ele pode ser diminuído
print([4], valor_1)
