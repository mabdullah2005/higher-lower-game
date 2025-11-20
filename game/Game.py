from .Deck import Deck
from .Player import Player
from typing import List

class Game:

    def __init__(self, deck: Deck, players: List[Player]):
        if len(players) < 1 or len(players) > 4:
            raise ValueError("Player amount needs to be between 1 and 4 (inclusive)")
        else:
            self._deck = deck
            self._players = players
    
    def shuffle(self):
        self._deck.shuffle()
    
    def guess(self, player_index: int, guess: int):
        if guess not in (0, 1):
            raise ValueError("Give a valid guess input")
        elif player_index not in range(0, len(self._players)):
            raise ValueError("Player not in game")
        
        player = self._players[player_index]
        if not player.is_alive():
            print(f'{self._players[player_index].name} is already eliminated')
            return
        
        current_card_value = self._deck.current.value
        new_card = self._deck.draw()
        new_card_value = new_card.value

        correct = (guess == 1 and (new_card_value > current_card_value)) or (guess == 0 and (new_card_value < current_card_value))

        if correct:
            player.increment()
            print("Correctly Guessed!")
        else:
            player.decrement()
            print("Wrong Guess!")

    def display(self):
        for player in self._players:
            print(str(player))
    
    def end_of_each_round(self):
        for player in self._players:
            player.is_alive()
        
        self.display()
    
    def end_of_game(self):
        final_standing = sorted(self._players, key=lambda p: p.score, reverse=True)

        for i in range(0, len(final_standing)):
            print(f'{i+1}: {str(final_standing[i])}')
