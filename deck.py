# Deck of Cards Class. Maintains the cards available in the deck
# and has methods for interacting with the deck
    
import random

class Deck:
    def __init__(self):
        self._cards = [f"{rank}{suit}" for rank in "23456789TJQKA" for suit in "♠♥♦♣"]
        random.shuffle(self._cards)

    def draw_card(self):
        return self._cards.pop() if self._cards else None

    def count_remaining_cards(self):
        '''return the number of remaining cards'''
        return len(self._cards)

