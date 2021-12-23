

"""
Objetivo:
    explicitar os argumentos e seus valores na chamada de uma função

Observação:
    os argumentos podem ser colocados fora de ordem, pois isso é corrigido na impressão
"""

def mostrar_dados(pais, nacionalidade, cidade):
    return pais, nacionalidade, cidade

# Declaração
pessoa = mostrar_dados(nacionalidade='brasileiro', pais='Brasil', cidade='Teresina')
print(1, pessoa)

# Print
print(2, mostrar_dados(pais='Japão', cidade='não informado', nacionalidade='Japonês'))
