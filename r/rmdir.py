

from metodos_bdd.file_deleter import dir_file_deleter


def objetivo():
    """ Remover um diretório, contanto que ele esteja vazio """


if __name__ == '__main__':

    # Esse método foi chamado, pois ele contêm o método responsável por deletar pastas [ file_deleter.py ]
    dir_file_deleter(path='C:\\Users\\Conta secundária\\Desktop',
                     folder=True,
                     folder_name='pasta',
                     os='windows',
                     delete_folder=True)

    # EXEMPLO SIMPLIFICADO (Windows):    rmdir('C:\\Users\\Conta secundária\\Desktop\\pasta')
