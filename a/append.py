

"""
Objetivo:
    - Anexar qualquer tipo de classe à uma variável de classe lista

Observação:
    - Pode ser usado multiplamente em linha (separação por vírgula)
    - Dados iteráveis com + de 1 índice, quando adicionados por esse método, contam apenas como 1 índice

Relacionamento:
    @list
"""


def add_into_list(single_data, box_receiver, box_sender, value=None):

    this_message_error = 'Tipo de dado não é aplicável à conjuntos'

    try:
        if single_data:
            box_receiver.append(value)
        else:
            for data in box_sender:
                box_receiver.append(data)
    except TypeError:
        return this_message_error


if __name__ == '__main__':
    this_var = []
    this_var_other = {'b', 'c', 'd', 'e', 'f', 'g', ('h', 'i', 'j', 'k')}
    print(this_var)
    add_into_list(single_data=True, box_receiver=this_var, box_sender=None, value='a')
    print(this_var)
    add_into_list(single_data=False, box_receiver=this_var, box_sender=this_var_other, value=None)
    print(this_var)
