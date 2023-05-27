class MCRouletteChecker
    def __init__(self):
        next

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
