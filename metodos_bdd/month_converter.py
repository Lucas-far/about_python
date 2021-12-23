

def mtd_month_converter_int_str(month: int):
    """"""

    # These two vars need to have the same length, otherwise the loop below will fail on picking the right choice
    months = 'january,february,march,april,may,june,july,august,september,october,november,december'.split(',')
    months_int = [*range(1, 13)]

    counter = 0
    while counter < len(months):
        if month == months_int[counter]:
            return months[counter]
        else:
            counter += 1


if __name__ == '__main__':
    print(var := mtd_month_converter_int_str(month=12))
