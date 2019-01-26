
class Card:
    
    def __init__(self, facing_up=False):
        self.facing_up = facing_up
    

class MemoGame:

    def __init__(self):
        self.cards = [Card(), Card()]

    def face_up_card_at(self, position):
        self.cards[position].facing_up = True
    
    def count_facing_up(self):
        return sum([card.facing_up for card in self.cards]) 

