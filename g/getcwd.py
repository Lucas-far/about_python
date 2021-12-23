

"""
Objetivo:
    mostrar a rota atual acessado no OS

Observação:
    1. apesar de ser um método, ele retorna uma string, que pode ser concatenada com outras
"""

from os import chdir, getcwd

chdir('/home/lucas/Documents')

# declaração
print(rota := getcwd())      # /home/lucas/Documents
# print
print(getcwd())              # /home/lucas/Documents
# concatenação na rota
print(getcwd() + '/pasta/')  # /home/lucas/Documents/pasta/
