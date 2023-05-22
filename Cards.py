import random

class CardGame:
    def __init__(self):
        self.deck = []
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        self.deck = [(value, suit) for value in values for suit in suits]
        random.shuffle(self.deck)

    def deal_cards(self):
        if len(self.deck) < 4:
            self.create_deck()

        self.player_hand = [self.deck.pop(), self.deck.pop()]
        self.dealer_hand = [self.deck.pop(), self.deck.pop()]
