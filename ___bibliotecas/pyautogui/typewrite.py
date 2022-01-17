

"""
Objetivo:
    - Escrever textos onde for possível escrever (não escreve caracteres especiais)
"""


def type_something(*args):
    from pyautogui import typewrite
    for data in args:
        typewrite(data)


def type_something_v2(**kwargs):
    from pyautogui import typewrite
    for data in kwargs.values():
        typewrite(data)


def type_something_v3(*args, **kwargs):
    from pyautogui import typewrite

    for data in args:
        typewrite(data)

    for data in kwargs.values():
        typewrite(data)


if __name__ == '__main__':
    from pyautogui import typewrite
    type_something('Linguagem ', 'Python', '\n')
    type_something_v2(par_1='Linguagem ', par_2='Javascript', par_3='\n')
    type_something_v3('Linguagem ', 'Java', '\n', par_1='Linguagem ', par_2='Ruby')
    # Uso normal
    typewrite('\nLinguagem Python\nLinguagem Javascript\nLinguagem Java\nLinguagem Ruby', interval=0.1)
