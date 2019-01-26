from memo_game import MemoGame


# Only one symbol
def test_all_cards_facing_down():
    assert MemoGame().count_facing_up() == 0


def test_should_be_able_to_flip_one_card():
    a_memo_game = MemoGame()

    a_memo_game.face_up_nth_card(1)

    assert a_memo_game.count_facing_up() == 1


def test_should_be_able_to_flip_two_cards():
    a_memo_game = MemoGame()

    a_memo_game.face_up_nth_card(1)
    a_memo_game.face_up_nth_card(2)

    assert a_memo_game.count_facing_up() == 2


def test_two_different_cards_should_face_back_down():
    a_memo_game = MemoGame(symbol_diversity=2)

    a_memo_game.face_up_nth_card(1)
    a_memo_game.face_up_nth_card(3)
    a_memo_game.rebase_cards()

    assert a_memo_game.count_facing_up() == 0


def test_two_equal_cards_should_keep_facing_up():
    a_memo_game = MemoGame(symbol_diversity=2)

    a_memo_game.face_up_nth_card(1)
    a_memo_game.face_up_nth_card(2)
    a_memo_game.rebase_cards()

    assert a_memo_game.count_facing_up() == 2


def test_only_two_cards_can_be_compared():
    a_memo_game = MemoGame(symbol_diversity=2)

    a_memo_game.face_up_nth_card(1)
    a_memo_game.face_up_nth_card(3)
    a_memo_game.face_up_nth_card(3)

    assert a_memo_game.count_facing_up() == 1


def test_the_game_is_complete():
    a_memo_game = MemoGame(symbol_diversity=2)

    a_memo_game.face_up_nth_card(1)
    a_memo_game.face_up_nth_card(2)
    a_memo_game.face_up_nth_card(3)
    a_memo_game.face_up_nth_card(4)

    assert a_memo_game.rebase_cards() == 'Game is finished'


def test_the_game_is_not_complete():
    a_memo_game = MemoGame(symbol_diversity=2)

    a_memo_game.face_up_nth_card(1)
    a_memo_game.face_up_nth_card(3)
    a_memo_game.face_up_nth_card(3)
    a_memo_game.face_up_nth_card(4)

    assert a_memo_game.rebase_cards() is None
