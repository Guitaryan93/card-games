# Player class keeps track of what the player is doing in the game of cards

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.total_value = 0

    def update_total_value(self):
        '''Calculate the total value of the cards in the players hand.'''  
        self.total_value = 0
        for card in self.hand:
            self.total_value += int(card[0])

    def show_hand(self):
        '''show cards in players hand'''
        print(f"{self.name}: ", end="")
        for card in self.hand:
            print(f"{card} ", end="")
        print()  # newline at the end
    


