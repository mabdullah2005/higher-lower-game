# Name: Card
# Description:
#   Holds all logic of a singular card

# Attributes:
#   suits: Tuple of all traditional suits found in a standard deck
#   ranks: Tuple of all traditional ranks found in a standard deck
#   suit: Suit of the card (eg/ Hearts, Diamonds, Clubs, Spades)
#   rank: Rank of the card (eg/ 2 - 10, Jack = 11, Queen = 12, King = 13, Ace = 1)
#   value: Value of Corresponding rank

class Card:
    _suits = ('Spades', 'Diamonds', 'Clubs', 'Hearts')
    _ranks = (
        'Ace',
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        'Jack',
        'Queen',
        'King'
    )

    _suit: str
    _rank: str 
    _value: int

    def __init__(self, suit:str, rank:str, value: int):
        if(suit not in self._suits):
            raise ValueError("Must be suitable suit")
        elif(rank not in self._ranks):
            raise ValueError("Must be suitable rank")
        elif(value > 13 or value < 1):
            raise ValueError("Must be suitable value")
        else:
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