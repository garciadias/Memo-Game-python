
class Card:

    def __init__(self, symbol, facing_up=False):
        self.facing_up = facing_up
        self.symbol = symbol


class MemoGame:

    def __init__(self, symbol_diversity=1):
        self.symbol_diversity = symbol_diversity
        self.cards = self.generate_cards(symbol_diversity)
        self.count_checks = 0
        self.last_tries = [None, None]

    def generate_cards(self, symbol_diversity):
        cards = []
        for symb in range(symbol_diversity):
            cards.extend([Card(symb), Card(symb)])
        return cards

    def check(self):
        symbol_1 = self.cards[self.last_tries[0]].symbol
        symbol_2 = self.cards[self.last_tries[1]].symbol
        return symbol_1 == symbol_2

    def face_up_nth_card(self, nth):
        # TODO: Manage nth that doesnt exist
        self.count_checks += 1
        if self.count_checks % 3 == 0:
            self.rebase_cards()
        self.cards[nth-1].facing_up = True
        self.last_tries[self.count_checks % 2] = nth-1

    def count_facing_up(self):
        return sum([card.facing_up for card in self.cards])

    def rebase_cards(self):
        if not self.check():
            self.cards[self.last_tries[0]].facing_up = False
            self.cards[self.last_tries[1]].facing_up = False
        if self.count_facing_up() == 2*self.symbol_diversity:
            return 'Game is finished'
