

"""
Objetivo:
    mudar diretório atual

Observação:
    1. esse método é pode ser mesclado com o método [ getcwd() ], que pertence a mesma biblioteca
    2. Sintaxe
        OS Windows
            rota: \\
            voltar rota: ..\\

        OS Ubuntu
            rota: /
            voltar rota: /../
"""

from os import chdir, getcwd

# @str

"No Windows"
# chdir('C:\\Users\\Lucas\\Downloads\\Main\\bdd_media')
# chdir('..')      # retorna um nível
# chdir('..\\..')  # retorna dois níveis

"No Ubuntu"
print(f'1 {getcwd()}')                                 # 1 /home/lucas/PycharmProjects/recursos/PYTHON/c
chdir(getcwd() + '/../')                               # Voltando um nível
print(f'2 {getcwd()}')                                 # 2 /home/lucas/PycharmProjects/recursos/PYTHON
chdir('/home/lucas/PycharmProjects/python_recursos/')  # Especificando o caminho manualmente
print(f'3 {getcwd()}')                                 # 3 /home/lucas/PycharmProjects/python_recursos
chdir(getcwd() + '/../' + '/../')                      # Voltando dois níveis
print(f'4 {getcwd()}')                                 # 4 /home/lucas
