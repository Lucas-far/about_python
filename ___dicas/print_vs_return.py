

def info():
    """
    1. [ print  ] é usado no escopo local da função, para não ser usado no escopo global
    2. [ return ] não é usado no escopo local da função, para ser usado no escopo global
    """


def f_print(dia, mes, ano):
    print(dia, mes, ano)


def f_return(dia, mes, ano):
    return dia, mes, ano


if __name__ == '__main__':
    f_print(1, 4, 2020)
    print(f_return(1, 4, 2020))
