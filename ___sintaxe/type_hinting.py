

"""
Objetivo:
    - Informar os tipos desejados em parâmetros de funções
    - Se a função possui retorno, serve para informar o retorno desejado
"""


def cacha_alta(sentence: list, separator: str) -> str:
    box = [str(each_data).upper() for each_data in sentence]
    return f"{separator}".join(box)


def show_your_data(name: tuple, birth: set, address: list, gender: str, disability: bool) -> dict:
    person_data = {
        'name': name, 'birth': birth, 'address': address, 'gender': gender, 'desability': disability
    }
    return person_data


if __name__ == '__main__':
    print(cacha_alta.__annotations__)
    print(show_your_data.__annotations__)
