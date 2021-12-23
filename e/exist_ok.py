

"""
Objetivo
    impedir a exibição de erro 'FileExistsError' em caso de tentativa repetida de criação de pasta

Observações
    1. funciona com o método makedirs(), mas não funciona com o método mkdir()
    2. makedirs() cria pastas aninhadas
    3. mkdir() cria uma pasta única separada
"""

from os import chdir, makedirs, mkdir

chdir('/home/lucas/Documents')

# TODO -> Testar cada contexto de forma separada (comentar #)

# Contexto que não gera erro
makedirs('mkdir/mkdir2', exist_ok=True)

# Contexto que gera erro (se executado + de 1 vez), pois [ exist_ok=bool ] funciona somente com o método [ makedirs ]
mkdir('mkdir')
makedirs('mkdir/mkdir2', exist_ok=True)
