

"""
Fonte:
     https://www.alt-codes.net

Procedimento no site:
    - Seleciona-se a imagem com o mouse, ctrl + c, ctrl + v na IDE

Objetivo:
    - Usar uma imagem como string
"""


def show_emoji_random():

    from random import choice
    emojis = ('♥', '☺', '☻', '♦', '♣')
    return choice(emojis)


if __name__ == '__main__':
    print(show_emoji_random())
