#YOUR COMBINED CLASSES

def __init__(self):
    self.result = None
    self.bet_amount = None
    self.bet_type = None

def spin_wheel(self):
    self.result = self.random.randint(0, 36)
    print(f"Roulette wheel has been spun. The pocket number is: {self.result}")

def take_bet(self, amount, bet_type):
    self.bet_amount = amount
    self.bet_type = bet_type
    print(f"Bet of {self.bet_amount} has been placed on {self.bet_type}.")

def play_game(self):
    if self.bet_amount is None or self.bet_type is None:
        print("Please place a bet first.")
    elif self.result is None:
        print("Please spin the wheel first.")
    else:
        if self.bet_type == 'number':
            if self.check_number_bet():
                print(f"Congratulations! You've won {self.bet_amount * 36}!")
            else:
                print("Sorry, you lost your bet.")
        elif self.bet_type == 'color':
            if self.check_color_bet():
                print(f"Congratulations! You've won {self.bet_amount * 2}!")
            else:
                print("Sorry, you lost your bet.")





#MY COMBINED CLASSES


import random

class Roulette:
    def __init__(self):
        self.pocket_number = 0
        self.bet = 0
        self.bet_type = ''
        self.pocket_colors = {**{i: 'red' for i in range(1, 11)},
                              **{i: 'black' for i in range(11, 21)},
                              0: 'green'}
                              
    def spin_wheel(self):
        self.pocket_number = random.randint(0, 20)

    def take_bet(self, amount, bet_type):
        self.bet = amount
        self.bet_type = bet_type

    def play_game(self):
        self.spin_wheel()
        print(f"Wheel landed on {self.pocket_number} {self.pocket_colors[self.pocket_number]}")
        if self.bet_type == 'number':
            self.check_number_bet()
        elif self.bet_type == 'color':
            self.check_color_bet()
        else:
            print("Invalid bet type")

    def check_number_bet(self):
        if self.bet == self.pocket_number:
            print("You won!")
        else:
            print("You lost!")
            
    def check_color_bet(self):
        if self.bet == self.pocket_colors[self.pocket_number]:
            print("You won!")
        else:
            print("You lost!")


#run game

game = Roulette()
game.take_bet(5, 'number')
game.play_game()
