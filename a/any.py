

"""
Objetivo:
    - Converter todos os dados dentro de variáveis iteráveis ou literais para booleano...
    - Se há pelo menos um dado = True, então o método retorna = True
    - Se todos os dados = False, então o método retorna = False

Observação:
    - Se o método receber um parâmetro que não é uma classe iterável, ele gera [ TypeError ]
"""


def turn_data_into_bool(data_list):

    this_msg_error = 'Há algum dado inválido.'

    box_data = []

    try:
        for data in data_list:
            box_data.append(any(data))

        return box_data
    except TypeError:
        return this_msg_error


if __name__ == '__main__':
    these = [{'': ''}, [], {}, '', ()]
    these2 = [{'': ''}, [], {}, '', (), 0]
    result = turn_data_into_bool(data_list=these)
    result2 = turn_data_into_bool(data_list=these2)
    print(result)
    print(result2)
