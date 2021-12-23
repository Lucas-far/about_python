

"""
Objetivo:
    modificar a rota atual de um módulo, no OS

Sintaxe:
    move('par1 = rota atual do módulo + nome do módulo + formato', 'par2 = nova rota do módulo')

Observação:
    1. sintaxe de rota para o Windows: \\
    2. sintaxe de rota para o Ubuntu: /
    3. a escrita da rota pode ser toda em minúscula, mas não deve conter erros de digitação
"""

from shutil import move

"move('C:\\Users\\Lucas\\Downloads\\a.png', 'C:\\Users\\Lucas\\Downloads\\main')"  # sintaxe em Windows
move('/home/lucas/Pictures/a.png', '/home/lucas/Videos')                           # sintaxe em Ubuntu
