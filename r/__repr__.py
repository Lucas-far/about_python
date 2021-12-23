

"""
Objetivo:
    função que apresenta dados para quando imprime-se um objeto instanciado

Observação:
    1. quando imprime-se um objeto com a ausência desse método na classe, mostra-se, ao invés, um objeto de memória
    2. recomenda-se ter nesse método, os atributos de instância definidos
    3. nesse método, aceita-se somente classe string, caso contrário gera-se: TypeError
"""

class Livro:
    def __init__(self, autor, titulo):
        self.__autor = autor
        self.__titulo = titulo

    def __repr__(self):
        return \
            f"""
            ======= Dados do Livro =======
            1. Nome do autor: {self.__autor}
            2. Autor do livro: {self.__titulo}
            """

livro = Livro('John Alfriad', 'A herva maligna')
print(livro)
