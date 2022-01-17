

"""
Objetivo:
    - Criar arquivos e adicionar conteúdo neles

Observação:
    - Pode ser combinada com o método de leitura: [read()]
    - O parâmetro 'a' remete à criação continuada de conteúdo ao arquivo alvo
    - O parâmetro 'w' (não usado aqui) remete à substituição continuada de conteúdo ao arquivo alvo

Relacionamento:
    @open()
"""


def write_something(whole_content, want_to_read, file_path, file_name, content='',  **kwargs):

    from os import chdir

    chdir(file_path)

    if whole_content:
        with open(file_name, 'a') as sheet:
            sheet.write(content + '\n')

        if want_to_read:
            with open(file_name, 'r') as sheet:
                for sentence in sheet:
                    print(sentence)

    else:
        with open(file_name, 'a') as sheet:
            for data in kwargs.values():
                sheet.write(data + '\n')

        if want_to_read:
            with open(file_name, 'r') as sheet:
                for sentence in sheet:
                    print(sentence)


if __name__ == '__main__':
    this_one = 'C:\\Users\\lucasf\\PycharmProjects\\python_everything\\w'
    this_one_as_well = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam
    nonummy auctor massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
    Nulla at risus. Quisque purus magna, auctor et, sagittis ac, posuere eu, lectus. Nam mattis, felis ut adipiscing.
    """

    write_something(whole_content=True,
                    want_to_read=False,
                    file_path=this_one,
                    file_name='metodo_write_demonstracao.txt',
                    content=this_one_as_well)

    write_something(whole_content=False,
                    want_to_read=True,
                    file_path=this_one,
                    file_name='metodo_write_demonstracao2.txt',
                    part_1='Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
                    part_2='Etiam eget ligula eu lectus lobortis condimentum.',
                    part_3='Aliquam nonummy auctor massa',
                    part_4='Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.',
                    part_5='Nulla at risus.',
                    part_6='Quisque purus magna, auctor et, sagittis ac, posuere eu, lectus.',
                    part_7='Nam mattis, felis ut adipiscing.')
