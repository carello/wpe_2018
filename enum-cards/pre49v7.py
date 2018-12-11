from enum import Enum
import random
import re


class CardValue(Enum):
    Deuce = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14

    def __str__(self):
        return f'{self.value}'


class CardSuit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

    def __str__(self):
        return f'{self.name}'


class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return repr(self.suit) + repr(self.value)

    def __str__(self):
        return f'{self.value} of {self.suit}'

    @staticmethod
    def string_split_by_numbers(x):
        r = re.compile('(\d+)')
        my_l = r.split(x)
        return [int(y) if y.isdigit() else y for y in my_l]

    @staticmethod
    def get_key(suits):
        # Adding string_split func if desired to add capabilities later.
        return Card.string_split_by_numbers(str(suits.suit)),\
               Card.string_split_by_numbers(str(suits.value))


if __name__ == '__main__':
    get_deck = [Card(suit, value)
                for value in CardValue for suit in CardSuit]
    hand = [str(card)
            for card in sorted(random.sample(get_deck, 5), key=Card.get_key)]

    print(f"{hand}\n")

    # Printing out a user friendly different format...
    for h in hand:
        sep = h.split()
        if sep[0] == '14':
            print(h.replace(sep[0], "A"))
        elif sep[0] == '11':
            print(h.replace(sep[0], "J"))
        elif sep[0] == '12':
            print(h.replace(sep[0], "Q"))
        elif sep[0] == '13':
            print(h.replace(sep[0], "K"))
        else:
            print(' '.join(sep))
    print()
