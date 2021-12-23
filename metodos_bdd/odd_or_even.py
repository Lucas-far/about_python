

def mtd_odd_or_even(integer: int):
    """"""

    integer = int(integer)

    if not integer % 2:
        return f'O número {integer} é par'
    else:
        return f'O número {integer} é ímpar'


if __name__ == '__main__':
    print(var := mtd_odd_or_even(integer=3.6))
