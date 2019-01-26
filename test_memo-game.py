"""Game setup

    All cards are facing down
"""

from memo_game import MemoGame

def test_all_cards_facing_down():
    assert MemoGame().facing_up() == 0
