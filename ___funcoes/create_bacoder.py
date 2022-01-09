

def mtd_create_bar_code():

    from random import choice

    void = []
    ints = tuple(range(0, 10))
    length = 13
    while length > 0:
        void.append(choice(ints))
        length -= 1

    void = [str(integer) for integer in void]
    # print(void)
    return ''.join(void)


if __name__ == '__main__':
    var = mtd_create_bar_code()
    print(var)
