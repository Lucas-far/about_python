

"""
Objetivo:
    - Tornar todas as letras de dados string como cacha alta

Observação:
    - Pode ser usado em outros iteráveis, contanto que neles só haja dados string

Relacionamento:
    @str
"""


def turn_data_uppercased(data):

    this_msg_error = 'O método só aceita dados iteráveis onde todos sejam string'
    this_msg_error2 = 'O tipo de dado informado não é aceitável'

    # box = []

    types_box = ("<class 'dict'>", "<class 'list'>", "<class 'set'>", "<class 'str'>", "<class 'tuple'>")

    # mandatory_type = types_box[3]

    # Todos os tipos são inseridos e é esperado todos devem sejam iguais: classe string
    # for index in data:
    #     box.append(type(index))

    # Certificar que há apenas um resultado
    # must_be_only_one_type = len(set(box))

    # E que este resultado seja uma string
    # is_string = str(tuple(set(box))[0])

    data_type = str(type(data))

    try:

        # Deve ter somente uma classe e ela deve ser string
        # if must_be_only_one_type == 1 and mandatory_type == is_string:

        # Outras formas de condição gerarão erro ou precisariam de muito mais condições, esta é a mais viável
        if data_type == types_box[0]:
            return {index[0].upper(): index[1].upper() for index in data.items()}
        elif data_type == types_box[1]:
            return [index.upper() for index in data]
        elif data_type == types_box[2]:
            return {index.upper() for index in data}
        elif data_type == types_box[3]:
            return data.upper()
        elif data_type == types_box[4]:
            return tuple((index.upper() for index in data))
        else:
            return this_msg_error2

    except AttributeError:
        return this_msg_error


if __name__ == '__main__':
    dict_ = {'nome': 'Alvaro', 'sexo': 'masculino'}
    list_ = ['Linguagem', 'Python']
    set_ = {'Linguagem', 'Python'}
    string_ = 'Linguagem Python'
    tuple_ = ('Linguagem', 'Python')
    print(turn_data_uppercased(dict_))
    print(turn_data_uppercased(list_))
    print(turn_data_uppercased(set_))
    print(turn_data_uppercased(string_))
    print(turn_data_uppercased(tuple_))

    dict_2 = {'nome': 'Alvaro', 'sexo': 'masculino', 'deficiência': False}
    print(turn_data_uppercased(dict_2))
