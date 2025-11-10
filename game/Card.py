# Name: Card
# Description:
#   Holds all logic of a singular card

# Attributes:
#   suit: Suit of the card (eg/ Hearts, Diamonds, Clubs, Spades)
#   rank: Rank of the card (eg/ 2 - 10, Jack = 11, Queen = 12, King = 13, Ace = 1)
#   value: Value of Corresponding rank

class Card:
    _suit: str
    _rank: str 
    _value: int

    def __init__(self, rank:str, suit:str, value: int):
        self._suit = suit
        self._rank = rank
        self._value = value

    @property
    def suit(self):
        return self._suit 

    @property
    def rank(self):
        return self._rank 
    
    @property
    def value(self):
        return self._value

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)   