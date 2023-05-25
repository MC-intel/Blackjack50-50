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
