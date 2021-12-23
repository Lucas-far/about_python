

def infos():
    """
    Módulo
        testar_em_docstring.py

    Objetivo:
        inserir testes em métodos através de suas docstrings

    Palavra chave
        testar docstring
    """


def obs():
    """
    1 - A sintaxe de nome 'assert' abaixo é opcional em docstrings
    2 - A sintaxe de nome 'assert' costuma ser a forma mais básica de teste
    3 - A sintaxe de nome 'assert' pode receber uma string ao final, para indicar uma resposta em caso de erro
    """

"""
>>> assert count_characters('banana') 'contagem errada'
    a: 3
    b: 1
    n: 2
"""


def count_characters(text):
    """
    >>> assert count_characters('banana')
    a: 3
    b: 1
    n: 2
    """

    from collections import Counter

    each_letter = sorted("".join(text.split()))  # Ex: text = banana    ['a', 'a', 'a', 'b', 'n', 'n']
    print(each_letter)
    letter_countage = dict(Counter(each_letter))  # ['a', 'a', 'a', 'b', 'n', 'n'] turns into {'a': 3, 'b': 1, 'n': 2}
    print(letter_countage)

    for key, value in letter_countage.items():
        print(key + ':', value)


if __name__ == '__main__':
    count_characters(text='banana')
