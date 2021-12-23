

from collections import Counter
from random import choice


def infos():
    """ Exemplificar as sintaxes [ , / ] e [ *, ] para impedir e obrigar o uso de arg. posicionado respectivamente """


# Função normal (argumentos posicionados são livres para serem usados ou descartados)
def create_dictionary(key, value):
    return {key: value}


# Função com sintaxe [ , / ] para impedir a chamada de argumentos nomeados
def invert_text(text: str, /):
    return text[::-1]


# Função com sintaxe [ *, ] para obrigar a chamada de argumentos posicionados
def count_letters(*, text: str):
    text_letters = dict(Counter(text))
    return text_letters


# Exemplo de função que usa ambas sintaxes
def send_a_message(from_, to_, /, subject='Não especificado', *, message):

    the_message = f"""
    --------------- {subject} ---------------
    {from_}
    {to_}
    {message}"""

    return the_message


if __name__ == '__main__':
    print(create_dictionary(key='linguagem', value='Python'))
    print(invert_text('Python'))                               # A sintaxe (, /) desativa arg. posicionado
    print(count_letters(text='Python'))                        # A sintaxe [ *, ] obriga o uso de arg. posicionado

    # Exemplo de função com ambas sintaxes: [ , / ] e [ , * ]. Note que os 2 primeiros pars estão sem arg. posicionado
    print(send_a_message('email1@gmail.com',
                         'email2@gmail.com',
                         subject='Ratos e esquilos',
                         message='Ratos são primos dos esquilos'))
