

def mtd_shuffle_list(data: list) -> str:

    from random import shuffle

    shuffle(data)
    return "".join(data)


if __name__ == '__main__':
    from random import shuffle
    keys = [*'1.2.3.4.5.6.7.8.9.0'.split('.'), '-']

    skills_wi = [
        'crystal cannon', 'fire cannon', 'fire lance', 'freeze', 'freezing arrow', 'freezing lance', 'ice blast',
        'wind arrow', 'wind blast', 'wind cannon', 'wind lance',
    ]

    skills_gl = [
        'Chakram slam', 'Illusion Blade', 'Fadeaway', 'Eternal Slash', 'Dread', 'Vital charge', 'Art of rage',
        'Sight Increase', 'Chakram slam 2', 'Illusion Blade 2', 'Fadeaway 2', 'Eternal Slash 2',
    ]
    shuffle(keys)
    shuffle(skills_gl)
    print(keys)
    print(skills_gl)
    # var = mtd_shuffle_list(data=target)
    # var2 = mtd_shuffle_list(data=target)
    # var3 = mtd_shuffle_list(data=target)
    # shuffle(skills)
    # print(f"{var}    {var2}    {var3}    SKILLS {skills}")
