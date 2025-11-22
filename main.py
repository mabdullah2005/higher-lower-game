# Name: main

# Description: 
#     main file holding the logic of the CLI loop.

from game.Game import Game
from game.Player import Player

print("Welcome to the Higher-Lower Game!")
print("\nDescription:")
print(f'\tEach player starts with 3 points. Players take turns in guessing whether the next card\'s rank value is higher or lower than the current card drawn. \n\n\tThey gain a point for guessing the player correctly and they lose a point for incorrect guesses.\n\n\tA player is eliminated if they reach 0 points. Last Player Standing Wins.\n')
print(f'\tNumbered values are the same as their rank.\n\nAll special cards\' (Jack, Queen, King) values range from 11 to 13. Aces have a value of 1.\n')
print(f'\n\nOne more thing... \n\tThere is a Joker in the deck...\n\t\tDraw it and the player is ELIMINATED with the points they have.\n\n')

active = True

while active:
    num_of_players = int(input("Specify the amount of players in the game (Min: 2, Max:4): "))
    
    while num_of_players not in range(2,5):
        num_of_players = int(input(f'\nRemember, 2-4 players are required. Specify the amount: '))

    players = []

    for i in range(0, num_of_players):
        name = input(f'Name of player {i+1}:\n')
        while len(name)==0:
            name = input(f'A player\'s name cannot be empty. What is player {i+1}\'s name: ')

        players.append(Player(name))

    game = Game(players)
    game_loop = True
    
    while(game_loop):
        game.simulate_round()
        game.end_of_each_round()

        if(game.no_player_alive_check()):
            game_loop = False
            game.end_of_game()
            another_game = int(input("Would you like to play another game? Yes(1) or No(Any other number):"))
            
            if(another_game != 1):
                active = False
                print(f'\nHave a great rest of your day!')
                continue       