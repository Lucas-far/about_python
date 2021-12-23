

def objetivo():
    """ Mostrar que por uma chave de um dicionário aninhado, é possível chamar seus dados de forma aleatória """


if __name__ == '__main__':
    from random import choice

    cadastro = {
        'nome': ['Ana', 'Ena', 'Ina', 'Ona'],
        'cidade': ['SP', 'PI', 'RJ', 'PR'],
        'idade': [19, 20, 21, 22]
    }

    #     1               2                  3
    print(cadastro['nome'][choice([*range(0, len(cadastro['nome']))])])

    #     1                 2                  3
    print(cadastro['cidade'][choice([*range(0, len(cadastro['cidade']))])])

    #     1                2                  3
    print(cadastro['idade'][choice([*range(0, len(cadastro['idade']))])])

    def explicacoes():
        """
        1 - A chamada das chaves
        2 - A chamada do método choice(), que está dentro de [], pois ele chama um índice, que chamada um dos dados
        3 - Note que é formado um range(0, 4), pois o tamanho de dados que há na chave ['nome'] acima, são 4
        """
