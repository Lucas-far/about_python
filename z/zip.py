

def objetivo():
    """
    Unir dados dentro de iteráveis baseado nos seus índices
    Número de índices devem ser iguais
    Vários iteráveis podem ser incluídos, contanto que tenha mesma quantidade de índices
    Os iteráveis são juntados em forma de tupla
    Se iteráveis a serem unidos não possuirem mesma quantidade, para mais: excedente ignorado
    Se iteráveis a serem unidos não possuirem mesma quantidade, para menos: ausente não é criado
    """


def give_a_grade():
    from random import choice

    box_grades = []
    lowest_grade = 0
    while lowest_grade < 10:
        box_grades.append(lowest_grade)
        lowest_grade += 0.1
    box_grades = [float(f"{number:.1f}") for number in box_grades]
    # print(box_grades)
    return choice(box_grades)


# Poderiam ser vários parâmetros, mas aqui será usado somente dois
def merge_iterables(type_iterable, box, box2):
    if type_iterable == 'conjunto':
        return set(zip(box, box2))
    elif type_iterable == 'dicionário':
        return dict(zip(box, box2))
    elif type_iterable == 'lista':
        return list(zip(box, box2))
    elif type_iterable == 'tupla':
        return tuple(zip(box, box2))


if __name__ == '__main__':

    print(['tupla -> string'], merge_iterables(type_iterable='conjunto', box=(1, 2), box2='3'))    # ausente
    print(['tupla -> string'], merge_iterables(type_iterable='lista', box=(1, 2), box2='345'))     # excedente
    print(['conjunto -> dicionário'], merge_iterables(type_iterable='dicionário', box={1, 2}, box2={3: 3, 4: 4}))
    print(['lista -> tupla'], merge_iterables(type_iterable='tupla', box=[1, 2], box2=(3, 4)))

    # var1 = {'1', '2'}
    # var2 = {'3': None, '4': None}
    # var3 = ['5', '6']
    # var4 = ('7', '8')
    # print([2], exemplo2 := set(zip(var1, var2, var3, var4)))
    #
    # alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    # numeracao = list(range(1, 27))
    # print([3], exemplo3 := list(zip(alfabeto, numeracao)))
    #
    # texto = ['dia'] * 10
    # dias = tuple(range(1, 11))
    # mes = ['de janeiro'] * 10
    # print([4], exemplo4 := list(zip(texto, dias, mes)))
    #
    # # --------------------------------------- Zip mesclado ao list comprehension ---------------------------------------
    print('-----------------------------------------------------------------------------------------------------------')
    alunos = ['Ana', 'Ena', 'Ina']
    ingles_semestre_1 = [give_a_grade(), give_a_grade(), give_a_grade()]
    ingles_semestre_2 = [give_a_grade(), give_a_grade(), give_a_grade()]
    #
    # # Cáclculo da média
    print([5], ex_lista := [float(f"{(dados[0] + dados[1]) / 2:.1f}") for dados in zip(ingles_semestre_1, ingles_semestre_2)])  # [7.0, 7.5, 8.0]
    # print([6], ex_conjunto := {(dados[0], dados[1]) for dados in zip(alunos, ex_lista)})
    # print([7], ex_dicio := {dados[0]: dados[1] for dados in zip(alunos, ex_lista)})
    # print([8], ex_tupla := tuple(((dados[0], dados[1]) for dados in zip(alunos, ex_lista))))
