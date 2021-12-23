

from csv import reader  # Esse é o método alvo chamado
from os import chdir    # Esse método serve para alcançar o módulo alvo

chdir('C:\\Users\\Conta secundária\\Downloads')  # O local do módulo alvo é alcançado
with open('documento_csv.csv', 'r') as doc:      # O módulo existente é chamado, e uma var para ele é criada
    leitura = reader(doc)                        # A var do módulo alvo é passada como argumento do método alvo

    # ----------------------------------------------- Leitura (parte 1) -----------------------------------------------
    # print(leitura)        # <_csv.reader object at...>
    # print(next(leitura))  # É criado uma lista onde o separador é cada vírgula no módulo csv

    # ----------------------------------------------- Leitura (parte 2) -----------------------------------------------
    # for each_data in leitura:
    #     print(each_data)

    # ----------------------------------------------- Leitura (parte 3) -----------------------------------------------
    for each_data in leitura:
        print(each_data[0])
        # print(each_data[1])
        # print(each_data[2])
