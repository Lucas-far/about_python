

def mtd_return_specific_value_from_list(target_list, wanted_data):
    """
    Get data from a list without the need of knowing its index
    It is recommended that there is no repeated data in the list, but if it is, the first one will be picked up
    The par1 is the list where you want to search
    The par2 is the value you want to get from the target list
    """

    data_acquired = target_list.pop(target_list.index(wanted_data))

    return data_acquired


if __name__ == '__main__':

    lista = ['Heleno', 'Almeida', 'Fonseca']
    name = mtd_return_specific_value_from_list(target_list=lista, wanted_data='Heleno')
    last_name = mtd_return_specific_value_from_list(target_list=lista, wanted_data='Almeida')
    print([1], name)
    print([2], last_name)
