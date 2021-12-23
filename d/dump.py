

from os import chdir
from pickle import dump, load

# Não faz parte do contexto, mas deseja-se fazer isso em outro local do sistema
chdir('/home/lucas/Documents')

class Dados:
    @staticmethod
    def vazio():
        return 'Eu sou um método inútil'

    @property
    def nome(self):
        return self.__nome

    def __init__(self, nome, idade, nacionalidade):
        self.__nome = nome
        self.__idade = idade
        self.__nacionalidade = nacionalidade

    def get_nome(self):
        return self.__nome

pessoa = Dados('Lucas', 27, 'brasileiro')

# O método [ dump() ] cria um módulo [ .csv ], para armazenar dados de uma variável objeto
with open('dados3.csv', 'wb') as doc:
    # dump(objeto, var with)
    dump(pessoa, doc)

# O método [ load() ] lê os dados do módulo [ .csv ] criado
with open('dados3.csv', 'rb') as doc2:
    leitura = load(doc2)
    print(leitura.vazio())
    print(leitura.nome)
    print(leitura.get_nome())
