

"""
Objetivo
    executar cálculo sequencial

Contexto
    1. cálculo sequencial de média
"""
# todo Tutorial 4

resultados = []

def calcular(valor, valor2):
    global resultados
    resultados.append(round(valor + valor2, 2))
    resultados.append(round(valor - valor2, 2))
    resultados.append(round(valor * valor2, 2))
    resultados.append(round(valor / valor2, 2))
    resultados.append(round(valor ** valor2, 2))

    return \
        """
        [ {} ] + [ {} ]  = [ {} ]
        [ {} ] - [ {} ]  = [ {} ]
        [ {} ] x [ {} ]  = [ {} ]
        [ {} ] / [ {} ]  = [ {} ]
        [ {} ] ** [ {} ] = [ {} ]
        """.format(
            valor, valor2, resultados[0], valor, valor2, resultados[1], valor, valor2, resultados[2],
            valor, valor2, resultados[3], valor, valor2, resultados[4]
        )

print(calcular(11, 9.2))
resultados.clear()
