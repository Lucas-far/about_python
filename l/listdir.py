

"""
Objetivo:
    mostrar uma lista dos diretórios e módulos existentes em uma rota especificada
"""

from os import chdir, listdir

chdir('/home/lucas/PycharmProjects/')    # muda-se para a rota desejada
print([1], l := listdir())               # todos os diretórios são apresentados em uma classe lista
print([2], l[0])                         # os dados podem ser acessados normalmente
print([3], tuple(enumerate(listdir())))  # os dados podem ser enumerados
print([4], [(i, x) for i, x in enumerate(l)])

def alternativo():
    counter = 0
    data = listdir()
    while counter < len(data):
        print(('Dado ' + str(counter), data[counter]))
        counter += 1
alternativo()
