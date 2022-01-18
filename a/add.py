

"""
Objetivo:
     - Anexar um novo dado à uma variável de classe conjunto

Observação:
    - Pode ser usado multiplamente em linha, se separado por vírgula
    - O método aceita somente um parâmetro por uso
    - Classe conjunto é intolerante às classes: conjunto, dicionário e lista

Relacionamento:
    @set
"""


def include_into_set(single_data, target, value=None, **kwargs):

    this_message_error = 'Tipo de dado não é aplicável à conjuntos'

    try:
        if single_data:
            target.add(value)
        else:
            for data in kwargs.values():
                target.add(data)
    except TypeError:
        return this_message_error


if __name__ == '__main__':
    a_set = set({})
    print(a_set)
    include_into_set(single_data=True, target=a_set, value='Python')
    print(a_set)
    include_into_set(single_data=False, target=a_set, key_1='Javascript', key_2='Ruby', key_3=None)
    print(a_set)
    include_into_set(single_data=True, target=a_set, value={'Python'})
    print(a_set)
