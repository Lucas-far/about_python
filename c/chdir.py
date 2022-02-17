

"""
Objetivo:
    - Mudar diretório atual

Relacionamento:
    @str

Observação:
    - No windows, a rota em string python usa o separador: \\
    - No ubuntu,  a rota em string python usa o separador: /

    - No windows, a string para retorno de nível é: ".." ou "..\\.." ou "..\\..\\.. (etc)
    - No ubuntu,  a string para retorno de nível é: "/../" + "/../" (etc)

Exemplos:
    ------- WINDOWS -------
    chdir('C:\\Users\\Lucas\\Downloads\\Main\\bdd_media') || Caminho com \\
    chdir(getcwd() + '..')                                || Retorno de um nível
    chdir(getcwd() + '..\\..')                            || Retorno de dois níveis

    ------- UBUNTU -------
    chdir('/home/lucas/PycharmProjects/python_recursos/') || Caminho com /
    chdir(getcwd() + '/../')                              || Retorno de um nível
    chdir(getcwd() + '/../' + '/../')                     || Retorno de dois níveis
"""


def change_location(os, where):
    from os import chdir, path, getcwd

    invalid_os = 'O sistema operacional não existe/é compatível.'
    invalid_path = 'O caminho especificado não existe.'
    invalid_type = 'Use comente dados string.'
    then = '------- Caminho anterior -------\n'
    now = '------- Caminho atual -------\n'

    systems = ('linux', 'windows')
    previous_path = getcwd()

    try:
        if os in systems:
            if path.exists(path=where):
                chdir(where)
                print(then + previous_path)
                print(now + where)
            else:
                print(invalid_path)
        else:
            print(invalid_os)
    except TypeError:
        print(invalid_type)


if __name__ == '__main__':
    change_location(os='windows', where='C:\\Users\\Lucasf\\Downloads')
    change_location(os='windows', where=None)
