

def objetivo():
    """ Contar quantos índice há dentro de chaves aninhadas em dicionários """


if __name__ == '__main__':

    cadastro = {
        'nome': ['Ana', 'Ena', 'Ina', 'Ona'],
        'cidade': ['SP', 'PI', 'RJ', 'PR'],
        'idade': [19, 20, 21, 22]
    }

    # O resultado neste caso é possível de saber, pois a lista é pequena, mas se fosse enorme, poderia ser feito:
    qtd_itens = sum([len(cadastro[chave]) for chave in cadastro])
