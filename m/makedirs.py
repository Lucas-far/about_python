

"""
Objetivo:
     criar pastas aninhadas, usando o separador de rota /

Observação:
    1. o método possui parâmetro 2, que evita erro: FileExistsError
"""

from os import chdir, makedirs

chdir('/home/lucas/Desktop/')
makedirs('pasta/pasta2/pasta3/pasta4/pasta5')
# Se a primeira pasta chamada, já existir, gera-se [ FileExistsError ], a não ser que haja [ exist_ok=True ]
makedirs('pasta/pasta5', exist_ok=True)
# A partir da segunda pasta, se ela já existe, ela é criada no mesmo nível da pasta 1, ao invés de aninhada
makedirs('pasta/pasta3', exist_ok=True)
