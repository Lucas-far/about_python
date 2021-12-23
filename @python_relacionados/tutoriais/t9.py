

"""
Objetivo:
    mostrar duas formas de fazer operação, nesse contexto: soma, em um loop for
"""
# todo Tutorial 9

def somar(*args):
    count = 0
    for each_number in args:
        count += each_number
    print(count)

somar(1, 7, 200)

def somar2(*args):
    print(sum(args))

somar2(1, 7, 200)
