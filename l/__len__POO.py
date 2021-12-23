

"""
Objetivo:
     retornar a quantidade de dados que uma classe iterável contêm

Observação:
    1. Quando o atributo de instância não é iterável: (ver class Livro & def __len__)
    2. Quando o atributo de instância é iterável: (ver class Livro2 & def __len__)
"""

class Livro:
    def __init__(self, nome, autor, folhas):
        self.__nome = nome
        self.__autor = autor
        self.__folhas = folhas

    def __len__(self):                                  # método __len__ funciona com iteráveis
        return self.__folhas                            # mas seu retorno não é um iterável
objeto = Livro('A herva maligna', 'John Alfriad', 172)  # objeto instanciado
print(len(objeto))                                      # para retorno do método não iterável: len() fora do escopo

class Livro2:
    def __init__(self, nome, autor, folhas):
        self.__nome = nome
        self.__autor = autor
        self.__folhas = folhas

    def __len__(self):                                 # método __len__ funciona com iteráveis
        return len(self.__autor)                       # seu retorno é um iterável
objeto2 = Livro2('A purificação', 'Laus Stranf', 802)  # objeto instanciado
print(len(objeto2))                                    # para retorno do método em iterável: len() dentro do escopo
