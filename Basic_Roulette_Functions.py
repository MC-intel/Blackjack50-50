 import random
 import Check_Roulette_values

class JORouletteFunctions:
  
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
                if Check_Roulette_values.check_number_bet():
                    print(f"Congratulations! You've won {self.bet_amount * 36}!")
                else:
                    print("Sorry, you lost your bet.")
            elif self.bet_type == 'color':
                if Check_Roulette_values.check_color_bet():
                    print(f"Congratulations! You've won {self.bet_amount * 2}!")
                else:
                    print("Sorry, you lost your bet.")
