

def mtd_temporizer(duration=5, the_user_path='/', the_alarm='file.format'):

    from os import chdir
    from time import sleep
    from webbrowser import open

    seconds = 0
    while seconds < duration:
        seconds += 1
        sleep(1)
        print(f'Atualmente em {seconds} segundos de {duration}. Faltando {duration - seconds} segundos para o término')

        if seconds == duration:
            chdir(the_user_path)
            open(the_alarm)
            break


if __name__ == '__main__':
    mtd_temporizer(duration=5,
                   the_user_path='C:\\Users\\Conta secundária\\Downloads',  # [ /home/lucas/Pictures/nature ]
                   the_alarm='eu.jfif')
