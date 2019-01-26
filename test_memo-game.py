from memo_game import MemoGame


def getRandomCardFrom(memoGame):
    all_cards = memoGame.get_all_cards()
    return all_cards[0]


def test_all_cards_facing_down():
    assert MemoGame().count_facing_up() == 0


def test_should_be_able_to_flip_one_card():
    aMemoGame = MemoGame()
    randomCard = getRandomCardFrom(aMemoGame)

    aMemoGame.face_up_card(randomCard)
    theCard = aMemoGame.get_card(randomCard)

    assert theCard.facing_up is True
