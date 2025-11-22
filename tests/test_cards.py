import pytest
from game.Card import Card

# Checks that cards of an invalid suit is not accepted
def test_valid_card_I():
    with pytest.raises(ValueError) as error:
        Card('Joe', 8, 8)

    assert str(error.value) == "Must be suitable suit"

# Checks that cards of an invalid rank is not accepted
def test_valid_card_II():
    with pytest.raises(ValueError) as error:
        Card('Spades', 14, 4)

    assert str(error.value) == "Must be suitable rank"

# Checks that cards of an invalid value is not accepted
def test_valid_card_III():
    with pytest.raises(ValueError) as error:
        Card('Clubs', 'King', 14)

    assert str(error.value) == "Must be suitable value"

# Checks that a Card with valid paremeters are accepted
def test_valid_card_IV():
    card = Card('Diamonds', 'Ace', 1)

    assert card is not None

# Testing how valid cards are displayed in the CLI
def test_card_string_format():
    card = Card('Hearts', 'Jack', 11)
    
    assert str(card) == "Jack of Hearts"