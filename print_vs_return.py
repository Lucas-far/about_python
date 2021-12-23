

def infos():
    """
    Objetivo
         formas de exibir dados vindos de uma função

    Observação
        1. [ print  ] é usado no escopo local da função, para não ser usado no escopo global
        2. [ return ] não é usado no escopo local da função, para ser usado no escopo global
    """

def f_print(dia, mes, ano):
    print(dia, mes, ano)
f_print(1, 4, 2020)


def f_return(dia, mes, ano=2020):
    return dia, mes, ano
print(f_return(1, 4))
