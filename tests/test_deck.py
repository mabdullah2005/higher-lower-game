import pytest
from game.Deck import Deck

@pytest.fixture
def deck():
    return Deck()

# As a Deck object is used in all of the unit tests below, a pytest.fixture was used to avoid constructing the deck multiple times. However, after a unit test is performed, the deck had to be cleared so it is ready to be tested again.

# Tests that a deck starts with 53 cards (1 is drawn to populate current card)
def test_deck_size_at_start(deck):
    assert len(deck.cards) == 53
    deck.clear()

# Tests that the current card is correctly populated as intended
def test_current_after_draw(deck):
    deck.draw()
    current_card = deck.current

    assert current_card is not None
    deck.clear()

# Tests that the deck of cards is correctly shuffled
def test_shuffle(deck):
    cards_before_shuffle = deck.cards[:]
    deck.shuffle()
    cards_after_shuffle = deck.cards[:]

    assert cards_before_shuffle != cards_after_shuffle
    deck.clear()

# Tests that shuffle works correctly after a card has been drawn
def test_shuffle_after_draw(deck):
    deck.draw()

    cards_before_shuffle = deck.cards[:]
    deck.shuffle()
    cards_after_shuffle = deck.cards[:]

    assert (
        len(cards_before_shuffle) == 52
        and len(cards_after_shuffle) == 52
        and (cards_before_shuffle != cards_after_shuffle)
    )
    deck.clear()