import pytest
from game.Deck import Deck

@pytest.fixture
def deck():
    return Deck()

def test_deck_size_at_start(deck):
    assert len(deck.cards) == 52
    deck.clear()

def test_current_at_start(deck):
    current_card = deck.current

    assert current_card is None
    deck.clear()

def test_deck_size_after_draw(deck):
    deck.draw()

    assert len(deck.cards) == 51
    deck.clear()

def test_current_after_draw(deck):
    deck.draw()
    current_card = deck.current

    assert current_card is not None
    deck.clear()

def test_shuffle(deck):
    cards_before_shuffle = deck.cards[:]
    deck.shuffle()
    cards_after_shuffle = deck.cards[:]

    assert cards_before_shuffle != cards_after_shuffle
    deck.clear()

def test_shuffle_after_draw(deck):
    deck.draw()

    cards_before_shuffle = deck.cards[:]
    deck.shuffle()
    cards_after_shuffle = deck.cards[:]

    assert (
        len(cards_before_shuffle) == 51 
        and len(cards_after_shuffle) == 51 
        and (cards_before_shuffle != cards_after_shuffle)
    )
    deck.clear()