#!/usr/bin/env python3

import random
from enum import IntEnum, auto, unique


@unique
class CardSuit(IntEnum):
    HEARTS = auto()
    DIAMONDS = auto()
    CLUBS = auto()
    SPADES = auto()


@unique
class CardValue(IntEnum):
    ACE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()


class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __lt__(self, other):
        return (self.suit < other.suit and self.value < other.value)

    def __repr__(self):
        return f"{self.value.name} of {self.suit.name}"


deck = [Card(suit, value)
        for suit in list(CardSuit)
        for value in list(CardValue)]

print(random.sample(deck, 5))

