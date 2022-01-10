

from database import (command)


def show_database(database_):
    for data in database_:
        print(data)


def store_database(database_main, database_box):
    for data in database_main:
        database_box.append(data)


"The function below is specific to this database"


# Numbers at var [ indexes ] relate to the number of fields this database has
def json(target_table, json_table):

    index_counter = 0
    indexes = (0, 1, 2)  # from tuple database, nested indexes 0, 1, 2 will be called

    while index_counter < len(target_table):

        json_table.append(
            {
                'id': target_table[index_counter][indexes[0]],
                'nome': target_table[index_counter][indexes[1]],
                'nascimento': target_table[index_counter][indexes[2]],
            }
        )

        index_counter += 1


table_pessoas = []
table_pessoas_json = []
command.execute('SELECT * FROM pessoas;')

if __name__ == '__main__':

    label_no_json = '------- BANCO DE DADOS NÃO JSON -------'
    label_json = '------- BANCO DE DADOS JSON -------'

    "Chamar bdd manualmente"
    # for data in command:
    #     print(data)

    print(table_pessoas)
    print(table_pessoas_json)
    store_database(database_main=command, database_box=table_pessoas)
    json(target_table=table_pessoas, json_table=table_pessoas_json)
    print(label_no_json)
    show_database(database_=table_pessoas)
    print(label_json)
    show_database(database_=table_pessoas_json)
