

def somar_dados(iterable_):
    this_msg_error = 'Conjuntos bloqueiam dados repetidos, podendo alterar o valor da soma. Tente outro iterável.'
    this_msg_error_2 = 'Todos os dados da lista devem ter o mesmo tipo: numérico real ou inteiro.'

    acceptable_types = ("<class 'int'>", "<class 'float'>")

    try:
        type_iterable = str(type(iterable_))
        result = sum(iterable_)
        type_result = str(type(sum(iterable_)))

        if type_iterable == "<class 'set'>":
            return this_msg_error
        if type_result not in acceptable_types:
            return this_msg_error_2
        if type_result in acceptable_types:
            return result

    except TypeError:
        return this_msg_error_2


if __name__ == '__main__':
    par_set = {1, 7.7, -2.2, 5, 3}
    par_wrong_type = '1, 7.7, -2.2, 5, 3'
    par_list = [1, 7.7, -2.2, 5, 3]
    par_tuple = (1, 7.7, -2.2, 5, 3)

    print(somar_dados(iterable_=par_set))
    print(somar_dados(iterable_=par_wrong_type))
    print(somar_dados(iterable_=par_list))
    print(somar_dados(iterable_=par_tuple))
