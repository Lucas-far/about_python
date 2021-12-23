

"""
Objetivo:
    copiar um módulo, de seu caminho atual para duplicá-lo em outro

Observação:
    o método possui 2 args mandatórios
    no arg1, especifica-se o local exato do módulo a ser deslocado, além da sua extensão
    no arg2, especifica-se o caminho para qual o módulo será enviado

Sintaxe
    No OS Windows: \\
    No OS Ubuntu: /
"""

from shutil import copy

# @str

"Windows"
# copy('C:\\Users\\Lucas\\Desktop\\main\\type_media\\look_at_the_toilet_paper.mp4', 'C:\\Users\\Lucas\\Desktop')

"Ubuntu"
copy('/home/lucas/Documents/css_botao', '/home/lucas/Desktop')
