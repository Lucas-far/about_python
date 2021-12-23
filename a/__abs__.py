

# @complex @float @int
def infos():
    """
    Objetivo: converter classes numéricas de valor negativo para sua versão positiva
    Observação: em classe complexo, há apenas uma conversão de class_type, e não de valor
    """


def test_mtd_abs(class_type, data):

    ink, ink_end = '\033[1:31m', '\033[m'
    try:
        print(f'{class_type} / {data.__abs__()}')
    except AttributeError as error:
        print(f"{ink}{error}{ink_end}")


if __name__ == '__main__':
    from python_types.all_types import *
    test_mtd_abs(class_type='booleano', data=type_boolean)
    test_mtd_abs(class_type='complexo', data=-type_complex)
    test_mtd_abs(class_type='dicionário', data=type_dict)
    test_mtd_abs(class_type='flutuante', data=type_float_n)
    test_mtd_abs(class_type='inteiro', data=type_integer_n)
    test_mtd_abs(class_type='lista', data=type_list)
    test_mtd_abs(class_type='nenhum', data=type_none)
    test_mtd_abs(class_type='range', data=type_range)
    test_mtd_abs(class_type='conjunto', data=type_set)
    test_mtd_abs(class_type='string', data=type_string)
    test_mtd_abs(class_type='tupla', data=type_tuple)
