

from database import (command)

table_pessoas = []
table_pessoas_json = []
command.execute('SELECT * FROM pessoas;')

if __name__ == '__main__':
    for data in command:
        print(data)
        table_pessoas.append(data)

    print(table_pessoas)

    list_length = 0
    index0 = 0
    index1 = 1
    index2 = 2

    while list_length < len(table_pessoas):
        # table_pessoas[0][0]
        # table_pessoas[0][1]
        # table_pessoas[0][2]
        table_pessoas_json.append(
            {
                'id': table_pessoas[list_length][index0],
                'nome': table_pessoas[list_length][index1],
                'nascimento': table_pessoas[list_length][index2],
            }
        )

        list_length += 1

    print(table_pessoas_json)
    for json in table_pessoas_json:
        print(json)
