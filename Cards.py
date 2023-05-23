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


#combined methods

import random

class BlackjackGame:
    def __init__(self):
        self.player_hand = []
        self.dealer_hand = []

    def calculate_score(self, hand):
        score = 0
        has_ace = False

        for card in hand:
            value = card[0]

            if value.isdigit():
                score += int(value)
            elif value in ['J', 'Q', 'K']:
                score += 10
            elif value == 'A':
                has_ace = True
                score += 1

        if has_ace and score + 10 <= 21:
            score += 10

        return score

    def play_game(self):
        self.create_deck()
        self.deal_cards()

        player_score = self.calculate_score(self.player_hand)
        dealer_score = self.calculate_score(self.dealer_hand)

        print("Player score:", player_score)
        print("Dealer score:", dealer_score)

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

# Create an instance of the game and play it
game = BlackjackGame()
game.play_game()

