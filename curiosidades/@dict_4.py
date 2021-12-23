

"""
Curiosidade? Usar dict comprehension e outros métodos
"""

from random import randint

tracks = [
    {'faixa': 'Chop Suey', 'nº de reproduções': randint(1, 1001)},
    {'faixa': 'Spiders', 'nº de reproduções': randint(1, 1001)},
    {'faixa': 'Toxicity', 'nº de reproduções': randint(1, 1001)},
    {'faixa': 'Vermilion pt2', 'nº de reproduções': randint(1, 1001)}
]


def metodo_1():
    # Dict comprehension de uma var contendo dicionários [ chave (int): valor (str) ]
    rank_most_played_unordered = {key['nº de reproduções']: key['faixa'] for key in tracks}

    # O método [ max() ] em iteráveis, retorna o maior valor contido, em dicionários, ele verifica as chaves
    most_played_song = max(rank_most_played_unordered)

    # O método [ get() ] é um método exclusivo dict, que por uma chave, retorna o seu respectivo valor
    most_played_song_name = rank_most_played_unordered.get(most_played_song)

    top_song = f"""
    ---------- MÚSICA MAIS TOCADA ----------
    {most_played_song_name} foi tocada {most_played_song} vezes"""

    print(rank_most_played_unordered)
    print(most_played_song)
    print(most_played_song_name)
    print(top_song)


def metodo_2():
    tracks_played_unordered_int = [key['nº de reproduções'] for key in tracks]
    most_played_track_int = max(tracks_played_unordered_int)

    # A lista matriz é percorrida p/ achar o int que coincida com [ most_played_track_int ], e retornando o seu valor
    most_played_track_str = ''.join([key['faixa'] for key in tracks if key['nº de reproduções'] == most_played_track_int])

    top_song = f"""
    ---------- MÚSICA MAIS TOCADA ----------
    {most_played_track_str} foi tocada {most_played_track_int} vezes
    """

    print(tracks_played_unordered_int)
    print(most_played_track_int)
    print(most_played_track_str)
    print(top_song)


def metodo_3():
    tracks_and_played_frequency = [(key['faixa'], key['nº de reproduções']) for key in tracks]

    #                                            tupla((str[0], int[1]))      ordenar pelo índice:    1   último índice
    tracks_and_played_frequency_ordered = sorted(tracks_and_played_frequency, key=lambda index: index[1])[-1]

    top_song = f"""
    ---------- MAIS TOCADA ----------
    {tracks_and_played_frequency_ordered[0]} foi tocada {tracks_and_played_frequency_ordered[1]} vezes"""

    print(tracks_and_played_frequency)
    print(tracks_and_played_frequency_ordered)
    print(top_song)


if __name__ == '__main__':
    metodo_1()
    metodo_2()
    metodo_3()
