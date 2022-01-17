

"""
Objetivo:
    - Atualizar dados em dicionário

Relacionamento:
    @dict
"""


def update_value_dict(display_it, the_dict, key, new_value):
    if display_it:
        the_dict.update({key: new_value})  # Uso aqui
        return the_dict[key]
    the_dict.update({key: new_value})  # Uso aqui


def update_value_dict_v2(display_it, the_dict, key, new_value):
    if display_it:
        the_dict[key] = new_value
        return the_dict[key]
    the_dict[key] = new_value


if __name__ == '__main__':

    # ---------- MÉTODO 1 ----------
    dict_ = {'linguagem': 'Javascript'}
    print(dict_)
    # Mudar sem guardar o valor novo
    update_value_dict(display_it=False, the_dict=dict_, key='linguagem', new_value='Ruby')
    print(dict_)
    # Mudar e guardar o valor novo
    get_new_value = update_value_dict(display_it=True, the_dict=dict_, key='linguagem', new_value='Python')
    print(dict_)

    print('-----------------------------------------------------------------------------------------------------------')

    # ---------- MÉTODO 2 ----------
    dict_2 = {'nome': 'Paulo'}
    print(dict_2)
    update_value_dict_v2(display_it=False, the_dict=dict_2, key='nome', new_value='Roberto')
    print(dict_2)
    get_new_value2 = update_value_dict_v2(display_it=True, the_dict=dict_2, key='nome', new_value='Moisés')
    print(dict_2)
