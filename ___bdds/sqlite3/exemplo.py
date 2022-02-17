

"""
Função 1: Criar os inicializadores que executam ações relacionados a banco de dados
Função 2: Criar um banco, com a ajuda da função 1
Função 3: Cria um objeto de um banco, com a ajuda das funções: 1 e 2
"""


def database_sqlite3_init(database_file_name: str):
    import sqlite3

    instance_ = sqlite3.connect(database_file_name)
    command_ = instance_.cursor()
    return instance_, command_


def create_sqlite3_database(database_name, name_pk, pk_type, fields_list, fields_list_len, exec_, instance_):
    """
    ---------- Example of result ----------
    CREATE TABLE IF NOT EXISTS hoteis(hotel_id text PRIMARY KEY, nome text, estrelas real, diaria real, cidade text)
    """

    invalid_table_size = 'Limite de campos para uma tabela excedidos: 10'
    table_created_success = '---------- TABELA CRIADA ----------\n{}'
    create_dtb = "CREATE TABLE IF NOT EXISTS {}({} {} PRIMARY KEY, ".format(database_name, name_pk, pk_type)
    closure = ")"
    fields = None

    if fields_list_len == 1:
        fields = "{}".format(fields_list)
    elif fields_list_len == 2:
        fields = "{} {}".format(*fields_list)
    elif fields_list_len == 3:
        fields = "{} {} {}".format(*fields_list)
    elif fields_list_len == 4:
        fields = "{} {} {} {}".format(*fields_list)
    elif fields_list_len == 5:
        fields = "{} {} {} {} {}".format(*fields_list)
    elif fields_list_len == 6:
        fields = "{} {} {} {} {} {}".format(*fields_list)
    elif fields_list_len == 7:
        fields = "{} {} {} {} {} {} {}".format(*fields_list)
    elif fields_list_len == 8:
        fields = "{} {} {} {} {} {} {} {}".format(*fields_list)
    elif fields_list_len == 9:
        fields = "{} {} {} {} {} {} {} {} {}".format(*fields_list)
    elif fields_list_len == 10:
        fields = "{} {} {} {} {} {} {} {} {} {}".format(*fields_list)
    else:
        print(invalid_table_size)

    create_dtb = create_dtb + fields + closure
    print(table_created_success.format(create_dtb))

    exec_.execute(create_dtb)
    instance_.commit()
    instance_.close()


def create_sqlite3_table_object(database_name, fields_list, fields_list_len, exec_, instance_):

    invalid_table_size = 'Limite de campos para uma tabela excedidos: 10'
    table_object_created_success = '---------- OBJETO DE TABELA CRIADO ----------\n{}'
    syntax_add = "INSERT INTO {} VALUES (".format(database_name)
    closure = ")"
    fields = None

    if fields_list_len == 1:
        fields = "'{}'".format(fields_list)
    elif fields_list_len == 2:
        fields = "'{}', '{}'".format(*fields_list)
    elif fields_list_len == 3:
        fields = "'{}', '{}', '{}'".format(*fields_list)
    elif fields_list_len == 4:
        fields = "'{}', '{}', '{}', '{}'".format(*fields_list)
    elif fields_list_len == 5:
        fields = "'{}', '{}', '{}', '{}', '{}'".format(*fields_list)
    elif fields_list_len == 6:
        fields = "'{}', '{}', '{}', '{}', '{}', '{}'".format(*fields_list)
    elif fields_list_len == 7:
        fields = "'{}', '{}', '{}', '{}', '{}', '{}', '{}'".format(*fields_list)
    elif fields_list_len == 8:
        fields = "'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'".format(*fields_list)
    elif fields_list_len == 9:
        fields = "'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'".format(*fields_list)
    elif fields_list_len == 10:
        fields = "'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'".format(*fields_list)
    else:
        print(invalid_table_size)

    create_this_object = syntax_add + fields + closure
    print(table_object_created_success.format(create_this_object))

    exec_.execute(create_this_object)
    instance_.commit()
    instance_.close()


if __name__ == '__main__':
    sqlite3_instance, sqlite3_command = database_sqlite3_init(database_file_name='sqlite3_database_v5.db')

    # TODO: Descomentar para criar banco
    # Sintaxe para [fields_list]: nome + espaço + tipo + vírgula + espaço
    # create_sqlite3_database(database_name='hoteis_v5',
    #                         name_pk='hotel_id',
    #                         pk_type='text',
    #                         fields_list=['nome text, ', 'estrelas real, ', 'diaria real, ', 'cidade text'],
    #                         fields_list_len=4,
    #                         exec_=sqlite3_command,
    #                         instance_=sqlite3_instance)

    # TODO: Descomentar para criar objeto de banco
    # Sintaxe para [fields_list]: nome
    # create_sqlite3_table_object(database_name='hoteis_v5',
    #                             fields_list=['legado', 'hotel legado', '4.9', '344', 'Uruçuí'],
    #                             fields_list_len=5,
    #                             exec_=sqlite3_command,
    #                             instance_=sqlite3_instance)
