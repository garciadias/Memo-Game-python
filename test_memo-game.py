from memo_game import MemoGame

def test_all_cards_facing_down():
    assert MemoGame().count_facing_up() == 0


def test_should_be_able_to_flip_one_card():
    a_memo_game = MemoGame()

    a_memo_game.face_up_card_at(0)
    
    assert a_memo_game.count_facing_up() == 1

def test_should_be_able_to_flip_two_cards():
    a_memo_game = MemoGame()

    a_memo_game.face_up_card_at(0)
    a_memo_game.face_up_card_at(1)
    
    assert a_memo_game.count_facing_up() == 2
