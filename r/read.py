

from os import chdir

chdir('C:\\Users\\Conta secundária\\Downloads')
with open('documento.txt', 'r') as doc:  # O arquivo não é criado, ele já deve existir. É criado apenas a sua var

    # ------------------------------------------------ Leitura (tipo 1) ------------------------------------------------
    # read_all = doc.read()  # A var chama o método de leitura
    # print(read_all)

    # ------------------------------------------------ Leitura (tipo 2) ------------------------------------------------
    # print(doc.read())

    # ------------------------------------------------ Leitura (tipo 3) ------------------------------------------------
    for each_data in doc:
        print(each_data, end='')
