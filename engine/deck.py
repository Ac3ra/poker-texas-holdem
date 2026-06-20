import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Deck:
    def __init__(self):
        self.cards = []
        self._build()

    def _build(self):
        suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.cards)
    