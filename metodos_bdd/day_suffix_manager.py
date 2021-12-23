

def mtd_day_suffix_manager(day: str):
    """"""

    suffixes = ('st', 'nd', 'rd', 'th')

    if day == '1':
        return day + suffixes[0]
    elif day == '2':
        return day + suffixes[1]
    elif day == '3':
        return day + suffixes[2]
    else:
        return day + suffixes[3]


if __name__ == '__main__':

    print(var := mtd_day_suffix_manager(day='1'))
    print(var2 := mtd_day_suffix_manager(day='2'))
    print(var3 := mtd_day_suffix_manager(day='3'))
    print(var4 := mtd_day_suffix_manager(day='4'))
