

"""
Objetivo
     retornar a data agora, neste momento, de forma geral (data e hora), ou específica (data ou hora)
"""

from datetime import datetime

# Uso de forma geral
print('hoje', data := datetime.now())  # print(data := datetime.today())

# Uso de forma especifica
print('ano', ano := datetime.now().year)
print('mês', mes := datetime.today().month)
print('dia', dia := datetime.now().day)
print('hora', hora := datetime.today().hour)
print('minuto', minuto := datetime.now().minute)
print('segundo', segundo := datetime.today().second)
print('microsegundo', microsegundo := datetime.now().microsecond)
print('dia da semana', dia_semana := datetime.today().weekday())     # Contagem inicia pelo índice 0 (dia da semana)
print('dia da semana', dia_semana2 := datetime.now().isoweekday())   # Contagem inicia pelo índice 1 (dia da semana)
