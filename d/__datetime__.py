

"""
Objetivo:
    Informar a data atual com todas as informações de tempo disponíveis

Objetivo 2:
    Customizar uma data para ser usada em cálculos

Observação:
    1. Dentro os 7 argumentos possíveis, os 3 primeiros são mandatórios e devem ser inteiros
    2. Há argumentos nomeados, mas estes são opcionais. A ordem não importa, pois na impressão, isso é corrigido
"""

from datetime import datetime

# Data agora
print(1, agora := datetime.now())
print(2, agora2 := datetime.today())

# Customizar uma data
print(3, data := datetime(1992, 7, 16, 12, 13, 14, 15))  # com todos os parâmetros possíveis
print(4, data2 := datetime(1992, 7, 16))                 # com os parâmetros obrigatórios

# Customizar uma data com argumentos nomeados (em ordem, ou fora de ordem)
print(5, data3 := datetime(year=1992, month=7, day=16, hour=12, minute=13, second=14, microsecond=15))
print(6, data4 := datetime(day=16, month=7, year=1992))

# Melhorar data customizada
print(7, data5 := datetime(2021, 1, 1))
print(8, data6 := str(datetime(2021, 1, 1)).split(' ')[0])  # poderia ser substituido pela var, mas quis fazer literal

# Calcular tempo
print(9, dias_de_vida := agora - data2)
