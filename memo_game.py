
class Card():
    
    def __init__(self, facing_up):
        self.facing_up = facing_up
    

class MemoGame():

    def __init__(self):
        pass

    def face_up_card(self, card):
        pass

    def get_card(self, card):
        return Card(facing_up=True)

    def count_facing_up(self):
        return 0

    def get_all_cards(self):
        return [Card(True)]