

def objetivo():
    """ Unir dados entre iteráveis baseado nos seus índices """

if __name__ == '__main__':
    lista = ['Nome', 'Sobrenome']
    tupla = 'Lucas', 'Farias'
    print([1], exemplo := tuple(zip(lista, tupla)))

    var1 = {'1', '2'}
    var2 = {'3': None, '4': None}
    var3 = ['5', '6']
    var4 = ('7', '8')
    print([2], exemplo2 := set(zip(var1, var2, var3, var4)))

    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    numeracao = list(range(1, 27))
    print([3], exemplo3 := list(zip(alfabeto, numeracao)))

    texto = ['dia'] * 10
    dias = tuple(range(1, 11))
    mes = ['de janeiro'] * 10
    print([4], exemplo4 := list(zip(texto, dias, mes)))

    # --------------------------------------- Zip mesclado ao list comprehension ---------------------------------------
    alunos = ['Ana', 'Ena', 'Ina']
    notas = [6.9, 7.9, 8.9]
    notas2 = [7.1, 7.1, 7.1]

    # Cáclculo da média
    print([5], ex_lista := [(dados[0] + dados[1]) / 2 for dados in zip(notas, notas2)])  # [7.0, 7.5, 8.0]
    print([6], ex_conjunto := {(dados[0], dados[1]) for dados in zip(alunos, ex_lista)})
    print([7], ex_dicio := {dados[0]: dados[1] for dados in zip(alunos, ex_lista)})
    print([8], ex_tupla := tuple(((dados[0], dados[1]) for dados in zip(alunos, ex_lista))))