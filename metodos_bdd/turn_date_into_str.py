

def mtd_turn_date_into_str(year: int = 1, month: int = 1, day: int = 1):
    """
    To take integers representing a date, and turn them into a text
    :param year:
    :param month:
    :param day:
    :return: string of the numbers representing the target date
    """

    months = 'janeiro,fevereiro,março,abril,maio,junho,julho,agosto,setembro,outubro,novembro,dezembro'.split(',')
    months_int = [*range(1, 13)]

    counter = 0

    while counter < len(months_int):
        if month == months_int[counter]:
            return f'{day} de {months[counter]} de {year}'
        else:
            counter += 1


if __name__ == '__main__':
    var = mtd_turn_date_into_str(year=1953, month=12, day=1)
    print(var)
