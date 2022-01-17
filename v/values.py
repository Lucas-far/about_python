

"""
Objetivo:
    - Exibir valores de chaves em dicionário, independente ou não de haver chaves aninhadas

Relacionamento:
    @dict
"""


def return_dict_values(is_nested, target_, main_key=None):

    this_msg_error = 'Tipo de dado aceitável: dicionário.'

    try:
        if is_nested:
            nested = tuple(nested_key for nested_key in target_[main_key].values())
            return nested
        else:
            not_nested = tuple(key for key in target_.values())
            return not_nested

    except AttributeError:
        return this_msg_error


if __name__ == '__main__':
    attemp_1 = {'dados': {'nome': 'Inácio', 'idade': 34, 'ciclista': True}}
    attemp_2 = {'nome': 'Python', 'paradigmas': 'Estrutural, orientado a objetos'}
    attemp_3 = [{'nome': 'Python', 'paradigmas': 'Estrutural, orientado a objetos'}]

    print(return_dict_values(is_nested=True, target_=attemp_1, main_key='dados'))
    print(return_dict_values(is_nested=False, target_=attemp_2))
    print(return_dict_values(is_nested=False, target_=attemp_3))
