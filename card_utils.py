# Utility class for comparing card values and other game related things
                                   
class CardUtils:                   
    def __init__(self, aces_value): 
        self.card_values = {"2": 2, 
                            "3": 3, 
                            "4": 4, 
                            "5": 5,         
                            "6": 6,
                            "7": 7, 
                            "8": 8,                              
                            "9": 9,
                            "T": 10,
                            "J": 11,                    
                            "Q": 12,
                            "K": 13,
                            "A": aces_value}
                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    def add_cards(self, cards_list):                                   
        '''Add together the value of all cards in cards_list.'''       
        total_value = 0                                                
        for card in cards_list:                                        
            total_value += self.card_values.get(card[0])               
            return total_value

