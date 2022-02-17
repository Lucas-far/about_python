

def letter_soup_paint(label: str):
    """"""

    from random import choice

    improper_type = 'Usar somente dado iterável: string'

    color_box: tuple = (
        '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[1:37m',
        '\033[1:38m',
    )

    allowed_type = ("<class 'str'>",)
    label_type = str(type(label))

    if label_type in allowed_type:
        letters_box = []

        for letter in label:
            letters_box.append(f"{choice(color_box)}{letter}{color_box[-1]}")

        letters_box = "".join(letters_box)
        return letters_box
    return improper_type


if __name__ == '__main__':
    print(letter_soup_paint(label='Python é uma linguagem de programação'))
    print(letter_soup_paint(label='Python é uma linguagem de programação'.split()))
    print(letter_soup_paint(label={'Python é uma linguagem de programação'}))
    print(letter_soup_paint(label=0))
