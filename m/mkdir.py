

"""
Objetivo:
     criar um diretório em uma rota no sistema operacional alvo

Observação:
    1. o método precisa do método chdir() para que seja escolhido a rota exata onde o diretório será criado
"""

from os import chdir, getcwd, mkdir

def criar_pasta(n_pastas_aninhadas=0):
    """ Gerar dentro de 1 pasta matriz, um número específico de pasta aninhadas """
    # Exemplo do método mkdir() através de um algoritmo criador de pastas
    pasta = 0
    pastas_criadas = 0
    while pasta < 1:
        chdir('/home/lucas/Desktop')                 # Mudança de diretório
        mkdir('pasta')                               # Criação de uma pasta com o nome "pasta"
        chdir(getcwd() + '/pasta/')                   # Mudança de diretório para a pasta que foi criada acima
        pasta += 1                                   # Encerramento do primeiro loop
        while pastas_criadas <= n_pastas_aninhadas:  # Inicio do segundo loop, criação das pastas aninhadas à matriz
            mkdir('pasta' + str(pastas_criadas))     # Criação de uma pasta chamada "pasta0"
            pastas_criadas += 1                      # Serão criadas: pasta1, pasta2, pasta3, etc...até o valor final

criar_pasta(7)
