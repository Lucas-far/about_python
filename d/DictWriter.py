

from os import chdir, getcwd
from csv import DictWriter

def infos():
    """
    Objetivo
         Criar módulo csv (arquivo de tabela com separação dos campos por meio de vírgula)
    """

chdir('/home/lucas/Documents')
print('Rota atual: ', getcwd())

with open('dados2.csv', 'w') as csv:

    # Primeiro, cria-se os dados de cabeçalho [ var = DictWriter(var interna, par=('campo', '...')) ]
    arquivo = DictWriter(csv, fieldnames=('Nome', 'Sobrenome', 'Idade', 'Nacionalidade'))

    # Cria-se o objeto, através de um dicionário, onde os campos são repetidos, e seus valores são definidos
    objeto1 = {'Nome': 'Lucas', 'Sobrenome': 'Farias', 'Idade': 27, 'Nacionalidade': 'brasileiro'}
    objeto2 = {'Nome': 'Alfredo', 'Sobrenome': 'Malaquias', 'Idade': 19, 'Nacionalidade': 'turco'}

    # Por último, os cabeçalhos e objetos criados precisam ser inseridos
    arquivo.writeheader()
    arquivo.writerow(objeto1)
    arquivo.writerow(objeto2)

    # Se na execução do script, nenhum erro for gerado, a criação do módulo csv foi feito com sucesso
