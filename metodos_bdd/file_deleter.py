

def mtd_file_deleter(path: str, folder: bool, folder_name: str, os: str, delete_folder: bool):
    """"""

    from os import listdir, remove, rmdir

    if folder and os == 'windows':
        box = listdir(path + '\\' + folder_name)
        label = box  # Backup of the [ box ] var, in order to show the list of the deleted files

        for file in box:
            remove(path + '\\' + folder_name + '\\' + file)

        print(show_deleted := f" -------------------- DELETED FILES --------------------\n{label}")

        if delete_folder:
            rmdir(path + '\\' + folder_name)

    if folder and os == 'ubuntu':
        box = listdir(path + '/' + folder_name)
        label = box  # Backup of the [ box ] var, in order to show the list of the deleted files

        for file in box:
            remove(path + '/' + folder_name + '/' + file)

        print(show_deleted := f" -------------------- DELETED FILES --------------------\n{label}")

        if delete_folder:
            rmdir(path + '/' + folder_name)

    else:
        print('Essa função é aplicável somente aos sistemas operacionais: Windows e Ubuntu')


if __name__ == '__main__':
    mtd_file_deleter(path='C:\\Users\\Conta secundária\\Desktop',
                     folder=True,
                     folder_name='pasta',
                     os='windows',
                     delete_folder=True)
