

"""
Objetivo:
    - Identar um dado de classe string para a direita

Relacionamento:
    @str
"""


def text_indent(text, indent_size):

    this_msg_error = 'Use somente dados inteiros positivos'
    this_msg_error2 = 'Use somente dados inteiros'

    try:
        if indent_size < 1:
            return this_msg_error
        return text.center(indent_size)
    except TypeError:
        return this_msg_error2


if __name__ == '__main__':
    print(text_indent(text='Python', indent_size=50))
    print(text_indent(text='Python', indent_size=None))
    print(text_indent(text='Python', indent_size=-50))
