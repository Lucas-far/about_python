

def infos():
    """
    Objetivo:
        /home/lucas/PycharmProjects/recursos/PYTHON/r/__repr__.py
    """

class Lapis:
    def __init__(self, marca, cor, expessura):
        self.__marca = marca
        self.__cor = cor
        self.__expessura = expessura

    # o retorno deve ser uma string (mandatório) e atributos de instância (opcional)
    def __str__(self):
        return 'Um lápis possui marca, cor, expessura'

lapis = Lapis('Faber Castle', 'cinza', 0.7)
print(lapis)
