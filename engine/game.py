from player import Player
from deck import Deck

DEFAULT_STACK = 50000

class Game:
    def __init__(self):
        self.deck = Deck()
        self.community_cards = []
        self.pot = 0
        self.turn = 0
        self.players = []
        self.players.append(Player([], DEFAULT_STACK, "Master Bator"))

        for player_count in range(1, 5):
            self.players.append(Player([], DEFAULT_STACK, f"Player {player_count}"))

    def deal_cards(self):
        for card_count in range(2):
            for player in self.players:
                player.cards.append(self.deck.cards[0])
                self.deck.cards.pop(0)

    def turn_flop(self):
        self.community_cards = self.deck.cards[:3]
        del self.deck.cards[:3]

    def turn_single_community_card(self):
        self.community_cards = self.deck.cards[0]
        del self.deck.cards[0]

    def start_game(self):
        self.deal_cards()
        