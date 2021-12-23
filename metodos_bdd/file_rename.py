def mtd_file_rename(where, fixed_syntax, the_format, integer, integer_random_sequence):
    """
    :param where:                   the path where the files are stored
    :param fixed_syntax:            fixed name for all files (pattern)
    :param the_format:              fixed file format for all the files
    :param integer:                 the number placed in each file name, increasing 1 by 1, at the end
    :param integer_random_sequence: in case the syntax stored in the name of the files is not progressive numbers
    :return:                        nothing, but shows iteration of each file name to show before and after the changes
    """

    from os import listdir, rename
    from random import choice

    before = '------------------------------------------------- ANTES -------------------------------------------------'
    after = '------------------------------------------------- DEPOIS -------------------------------------------------'
    place = listdir(where)

    print(before)
    for data in place:
        print(data, end='    ')
    print('\n')

    if integer_random_sequence:
        for file in place:
            code = choice(range(1111111111111, 9999999999999))
            rename(where + '\\' + file, where + '\\' + fixed_syntax + str(code) + the_format)

    else:
        for file in place:
            rename(where + '\\' + file, where + '\\' + fixed_syntax + str(integer) + the_format)
            integer += 1

    place = listdir(where)
    print(after)
    for data in place:
        print(data, end='    ')


if __name__ == '__main__':

    mtd_file_rename(where='C:\\Users\\Conta secundária\\Desktop\\teste',
                    fixed_syntax='',
                    the_format='.txt',
                    integer=None,
                    integer_random_sequence=True)
