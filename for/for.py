

# Testando todas as horas possíveis por (iterável + loop for)
def ex3() -> None:
    hora = [*range(0, 24)]
    for h in hora:
        if h in hora[0:12]:
            print(h, 'Bom dia')
        elif h in hora[12:18]:
            print(h, 'Boa tarde')
        elif h in hora[18:]:
            print(h, 'Boa noite')
    del hora

ex3()
