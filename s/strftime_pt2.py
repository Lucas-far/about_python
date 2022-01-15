

def informar_data():

    from datetime import datetime
    months_pt_br = [*'janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'.split()]
    months_eng_us = [*'January February March April May June July August September October November December'.split()]
    date_pattern = '%d/%B/%Y'  # %B insere o mês em inglês
    time_full = datetime.today()
    time_full_as_str = str(time_full.strftime(date_pattern))

    index = 0
    while index < len(months_pt_br):
        if months_eng_us[index] in time_full_as_str:
            return f'{time_full.day} de {months_pt_br[index]} de {time_full.year}'
        index += 1

    # conditions = {
    #     meses_eng_us[0] in agora_: f'{tempo.day} de {meses[0]} de {tempo.year}',
    #     meses_eng_us[1] in agora_: f'{tempo.day} de {meses[1]} de {tempo.year}',
    #     meses_eng_us[2] in agora_: f'{tempo.day} de {meses[2]} de {tempo.year}',
    #     meses_eng_us[3] in agora_: f'{tempo.day} de {meses[3]} de {tempo.year}',
    #     meses_eng_us[4] in agora_: f'{tempo.day} de {meses[4]} de {tempo.year}',
    #     meses_eng_us[5] in agora_: f'{tempo.day} de {meses[5]} de {tempo.year}',
    #     meses_eng_us[6] in agora_: f'{tempo.day} de {meses[6]} de {tempo.year}',
    #     meses_eng_us[7] in agora_: f'{tempo.day} de {meses[7]} de {tempo.year}',
    #     meses_eng_us[8] in agora_: f'{tempo.day} de {meses[8]} de {tempo.year}',
    #     meses_eng_us[9] in agora_: f'{tempo.day} de {meses[9]} de {tempo.year}',
    #     meses_eng_us[10] in agora_: f'{tempo.day} de {meses[10]} de {tempo.year}',
    #     meses_eng_us[11] in agora_: f'{tempo.day} de {meses[11]} de {tempo.year}',
    # }
    #
    # for key in conditions:
    #     if key:
    #         return conditions[key]


if __name__ == '__main__':
    print(informar_data())
