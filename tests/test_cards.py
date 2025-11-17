import pytest
from game.Card import Card

def test_valid_card_I():
    with pytest.raises(ValueError) as error:
        Card('Joe', 8, 8)

    assert str(error.value) == "Must be suitable suit"

def test_valid_card_II():
    with pytest.raises(ValueError) as error:
        Card('Spades', 14, 4)

    assert str(error.value) == "Must be suitable rank"

def test_valid_card_III():
    with pytest.raises(ValueError) as error:
        Card('Clubs', 'King', 14)

    assert str(error.value) == "Must be suitable value"

def test_valid_card_IV():
    card = Card('Diamonds', 'Ace', 1)

    assert card is not None

def test_card_string_format():
    card = Card('Hearts', 'Jack', 11)
    
    assert str(card) == "Jack of Hearts"