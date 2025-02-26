# Blackjack built with Python
#
# Gameplay loop:
# SETUP:
# - Player places a bet between $2 and $500
# - Deal 1 card to player face up
# - Deal 1 card to dealer face up
# - Deal 1 card to the player face up
# - Deal 1 card to the dealer FACE DOWN
#
# LOGIC:
# - If player cards == 21 then they win
# - Else if player cards are > 21 they lose
# - Else if player cards are < 21 they can stand or hit
#   - hit gives another card
#     - ace can be 1 or 11
#   - stand ends players turn
# - once player stands the dealer has a go
#   - The dealer must stand if 17 or more
#   - dealer must hit if 16 or less
#   - dealer cannot treat ace as 1 if total is over 17
#     they must stand


from deck import Deck
from player import Player
from card_utils import CardUtils

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.p1 = Player("Bob")
        self.p2 = Player("Dealer")
        self.players = [self.p1, self.p2]
        self.util = CardUtils(11)
        self.game_over = False
        while not self.game_over:
            self.initial_deal()
            self.show_hands()
            blah = input(">>>")
            #self.util.


    def deal_card(self, player):
        '''deal card to player'''
        player.hand.append(self.deck.draw_card())

    def initial_deal(self):
        '''deal the initial 2 cards per player
           one at a time'''
        for i in range(0,2):
            for p in self.players:
                self.deal_card(p)

    def show_hands(self):
        '''show all player hands'''
        for p in self.players:
            p.show_hand()


if __name__ == "__main__":
    game = Blackjack()

