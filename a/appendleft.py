

"""
Objetivo:
    - Anexar qualquer tipo de classe à uma variável de classe deque/lista, a partir do índice 0 (sempre)

Observação:
    - A classe [ deque ] têm a mesma biblioteca de métodos da classe [ lista ], mas com métodos adicionais
    - Pode ser usado multiplamente em linha (separação por vírgula)
    - Dados iteráveis com + de 1 índice, quando adicionados por esse método, contam apenas como 1 índice

Relacionamento:
    @deque
"""


def add_into_list_at_left(single_data, box_receiver, box_sender, value=None):

    from collections import deque

    this_message_error = 'Tipo de dado não é aplicável à conjuntos'

    try:
        box = deque([*box_receiver])
        print([1], box)

        if single_data:
            box.appendleft(value)
        else:
            for data in box_sender:
                box.appendleft(data)
        box_receiver = list(box)
        print([1.1], box)
        print([1.2], box_receiver)
    except TypeError:
        print(this_message_error)


if __name__ == '__main__':
    from collections import deque
    # NÃO ESTÁ FUNCIONANDO EM FUNÇÃO
    this_var = [True]
    this_var_other = {'b', 'c', 'd', 'e', 'f', 'g', ('h', 'i', 'j', 'k')}
    print([1.3], this_var)
    add_into_list_at_left(single_data=True, box_receiver=this_var, box_sender=None, value=False)
    print([1.4], this_var)
    add_into_list_at_left(single_data=False, box_receiver=this_var, box_sender=this_var_other, value=None)
    print([1.5], this_var)
    # FORA DA FUNÇÃO
    var = deque([])
    var.appendleft(this_var)
    print(var)
    var.appendleft(this_var_other)
    print(var)
