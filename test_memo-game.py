from memo_game import MemoGame


def getRandomCardFrom(memoGame):
    all_cards = memoGame.get_all_cards()
    return all_cards[0]


def test_all_cards_facing_down():
    assert MemoGame().count_facing_up() == 0


def test_should_be_able_to_flip_one_card():
    a_memo_game = MemoGame()
    random_card = getRandomCardFrom(a_memo_game)

    a_memo_game.face_up_card(random_card)
    the_card = a_memo_game.get_card(random_card)

    assert the_card.facing_up is True
