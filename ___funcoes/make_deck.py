

def mtd_make_deck(is_random: bool = True) -> list:
    """"""

    from random import shuffle

    symbols = ['♥', '♦', '♣', '♠']
    deck_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = []

    if is_random:
        deck = [(card + card2) for card2 in symbols for card in deck_values]  # exemplo aqui
        shuffle(deck)
        return deck
    else:
        deck = [(card + card2) for card2 in symbols for card in deck_values]
        return deck


if __name__ == '__main__':
    print(mtd_make_deck(is_random=False))
    print(the_deck := mtd_make_deck())
    print(len(the_deck))
