# Name: Game

# Description:
#     Holds all the logic of the game. Functionality includes displaying scores of players and simulating a round of guesses.

# Attributes:
#     deck: Standard deck of cards including 1 joker.
#     players: list of Player Objects within the game.


from .Deck import Deck
from .Player import Player
from typing import List

class Game:

    def __init__(self, players: List[Player]):
        self._deck = Deck()
        self._players = players

    def display(self):
        for player in self._players:
            print(str(player)) 

        print(f'\nCards left in play: {len(self._deck.cards)}')

    def shuffle(self):
        self._deck.shuffle()
    
    def guess(self, guess: int):        
        current_card_value = self._deck.current.value
        new_card = self._deck.draw()
        new_card_value = new_card.value
        
        print(f'Card Drawn: {self._deck.current}')
        
        if(self._deck.current.rank == 'JOKER'):
            return 'JOKER'

        correct = (guess == 1 and (new_card_value > current_card_value)) or (guess == 0 and (new_card_value < current_card_value))

        if correct:
            print(f'Correctly Guessed!\n')
            return True
        else:
            print(f'Wrong Guess!\n')
            return False
    #End of guess()
    
    def simulate_round(self):
        for player in self._players:
            if(player.player_alive):
                print(f'\nCurrent Card: {self._deck.current}')
                
                player_guess = int(input(f'{player.name}, Higher (1) or Lower(0)?'))
                while player_guess not in (0, 1):
                    player_guess = int(input("Give a valid guess input. Higher(1) or Lower(0)?"))

                result = self.guess(player_guess)
                if(result == 'JOKER'):
                    print(f'Sorry {player.name}, you have drawn a joker. You are Eliminated\n')
                    player.eliminate()
                    return

                if(result):
                    player.increment()
                else:
                    player.decrement()
    #end of simulate_round()

    def end_of_each_round(self):
        for player in self._players:
            player.check_alive()

        print("X" * 40)
        
        print('End of Round:')        
        self.display()

        print("X" * 40 + "\n")

        shuffle_choice = int(input("Would you like to shuffle the deck? Yes (1) or No(Any other number):"))
        if(shuffle_choice == 1):
            self._deck.shuffle()

    #end of end_of_each_round()

    def no_player_alive_check(self):
        players_alive = 0
        for player in self._players:
            if(player.player_alive):
                players_alive += 1
        
        if(players_alive == 0):
            return True
        return False
    #end of last_player_check()
    
    def end_of_game(self):
        final_standing = sorted(self._players, key=lambda p: p.score, reverse=True)

        print("X" * 100)
        print("\nFinal Standings:")
        for i in range(0, len(final_standing)):
            print("\t" * (i + 1) + f"{i+1}: {final_standing[i]}")
        print("\n" + "X" * 100)
