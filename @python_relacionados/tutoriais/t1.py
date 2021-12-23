

"""
Objetivo
    acessar um módulo csv existente, e mudar sua forma de exibição de dados através do recurso Python DictReader()

Observação
    1. o módulo csv existente continuar intacto
"""
# todo Tutorial 1

from os import chdir
from csv import DictReader

# Exemplo de módulo csv
"Nome,sobrenome,idade,nacionalidade"
"Lucas,Farias,27,brasileiro"
"Mário,Santos,33,polonês"
"Luigi,Sousa,41,peruano"

chdir('/home/lucas/Desktop/')

with open('dados.csv', 'r') as csv:
    with open('dados_dict.csv', 'w+') as dictionary:
        leitura = DictReader(csv)
        for each_data in leitura:
            dictionary.write(str(each_data))
            dictionary.write('\n')
