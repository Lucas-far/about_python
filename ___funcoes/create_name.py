

def mtd_created_name():

    from random import choice

    var = [
        'bra', 'bre', 'bri', 'bro', 'bru',
        'cha', 'che', 'chi', 'cho', 'chu',
        'lha', 'lhe', 'lhi', 'lho', 'lhu',
        'qua', 'que', 'qui', 'quo',
        'pra', 'pre', 'pri', 'pro', 'pru'
        'ssa', 'sse', 'ssi', 'sso', 'ssu',
        'sna', 'sne', 'sni', 'sno', 'snu',
        'tra', 'tre', 'tri', 'tro', 'tru',

        'ba', 'be', 'bi', 'bo', 'bu',

        'ca', 'ce', 'ci', 'co', 'cu',

        'da', 'de', 'di', 'do', 'du',

        'fa', 'fe', 'fi', 'fo', 'fu',

        'ga', 'ge', 'gi', 'go', 'gu',

        'ha', 'he', 'hi', 'ho', 'hu',

        'ja', 'je', 'ji', 'jo', 'ju',

        'ka', 'ke', 'ki', 'ko', 'ku',

        'la', 'le', 'li', 'lo', 'lu',

        'ma', 'me', 'mi', 'mo', 'mu',

        'na', 'ne', 'ni', 'no', 'nu',

        'pa', 'pe', 'pi', 'po', 'pu',

        'qa', 'qe', 'qi', 'qo', 'qu',

        'ra', 're', 'ri', 'ro', 'ru',

        'sa', 'se', 'si', 'so', 'su',

        'ta', 'te', 'ti', 'to', 'tu',

        'va', 've', 'vi', 'vo', 'vu',

        'wa', 'we', 'wi', 'wo', 'wu',

        'xa', 'xe', 'xi', 'xo', 'xu',

        'ya', 'ye', 'yi', 'yo', 'yu',

        'za', 'ze', 'zi', 'zo', 'zu',
    ]

    name = f'{choice(var)}{choice(var)}{choice(var)}{choice(var)}'.title()

    return name


if __name__ == '__main__':
    print(mtd_created_name())
    # box = [*'b.c.d.f.g.h.j.k.l.m.n.p.q.r.s.t.v.w.x.y.z'.split('.')]
    # # print(box)
    # index = 0
    # while index < len(box):
    #     quadro = f"""
    #     '{box[index]}a', '{box[index]}e', '{box[index]}i', '{box[index]}o', '{box[index]}u',
    #     '{box[index]}a'.upper(), '{box[index]}e'.upper(), '{box[index]}i'.upper(), '{box[index]}o'.upper(), '{box[index]}u'.upper(),
    #     """
    #     print(quadro)
    #     index += 1
