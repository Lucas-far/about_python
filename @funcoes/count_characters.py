

def mtd_count_characters(text):
    """"""

    from collections import Counter

    each_letter = sorted("".join(text.split()))  # Ex: text = banana    ['a', 'a', 'a', 'b', 'n', 'n']
    # print(each_letter)
    letter_countage = dict(Counter(each_letter))  # ['a', 'a', 'a', 'b', 'n', 'n'] turns into {'a': 3, 'b': 1, 'n': 2}
    # print(letter_countage)

    for key, value in letter_countage.items():
        print(key + ':', value)


if __name__ == '__main__':
    mtd_count_characters(text='banana')
