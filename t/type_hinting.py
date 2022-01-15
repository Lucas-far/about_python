

"""
Objetivo:
    - Informar os tipos desejados em parâmetros de funções
    - Se a função possui retorno, serve para informar o retorno desejado
"""


def cacha_alta(sentence: list, separator: str) -> str:
    box = [str(each_data).upper() for each_data in sentence]
    return f"{separator}".join(box)


if __name__ == '__main__':
    print(cacha_alta(sentence=['Eu', 'e', 'você'], separator='_'))
    print(cacha_alta.__annotations__)
