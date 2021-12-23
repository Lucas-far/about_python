

from csv import DictReader
from os import chdir, getcwd

def infos():
    """
    Objetivos
         Ler módulos csv já criados/existentes

    Observações
        1. O módulo csv não deve conter erros de digitação, e o formato deve ser explicitado
        2. O segundo argumento deve ser 'r', pois é a leitura de um módulo que já existe
    """

chdir('/home/lucas/Documents')
print('Rota atual: ', getcwd())

# Lendo todos os dados
with open('dados.csv', 'r') as csv:
    for each_data in DictReader(csv):
        print(each_data)

print('\n')

# Lendo dados de forma especificada (as chaves no módulo devem ser especificadas)
with open('dados.csv', 'r') as csv:
    # leitura = DictReader(csv)
    for each_data in DictReader(csv):
        print(each_data['nome'], each_data['idade'])
