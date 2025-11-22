from .Card import Card
import random

# Name: Deck
# Description:
#     Consists deck logic. Functionalities include creating a deck of cards, shuffling the deck, drawing a card from the deck and retrieving the current card that has been dawn

# Attributes:
#     suits: Tuple of all traditional suits found in a standard deck
#     cards: Array that holds all cards that have not been drawn
#     current: Current card that has been drawn

class Deck:
    _suits = ('Spades', 'Diamonds', 'Clubs', 'Hearts')
    _rankEquivalent = {
        1: 'Ace',
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 'Jack',
        12: 'Queen',
        13: 'King'
    }
    _current = None

    def __init__(self):
        self._cards = []
        self.create_deck()
        self.draw()

    def create_deck(self):
        self.clear()

        for x in self._suits:
            for y in range(1, 14):
                self._cards.append(Card(x, self._rankEquivalent.get(y), y))

        self._cards.append(Card('JOKER', 'JOKER', 1))
        self._cards.append(Card('JOKER', 'JOKER', 1))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if(len(self._cards) == 0):
            print(f'\n\nYou have reached the end of the deck. Deck is being reshuffled...\n\n')
            self.create_deck()
        
        self._current = self._cards.pop()
        return self._current

    @property
    def current(self):
        return self._current
    
    @property
    def cards(self):
        return self._cards
    
    def clear(self):
        self._cards.clear()
        self._current = None