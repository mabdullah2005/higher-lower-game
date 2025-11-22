Name:
    HIGHER-LOWER GAME

Author:
    Muhammad Haris Abdullah

Technology Used: Python (With Pytest for Unit Testing)

Skills Demonstrated:
    - Object-Oriented Programming
    - User Interaction
    - Unit Testing

Classes:
    - Card
    - Player
    - Deck
    - Game

Description:
    Created a Higher-Lower Card Game, showcasing my fundamental programming skills. developing this project in Python displays the transferability of my coding, as the combination of this project and the projects in my CV prove that I possess a strong understanding of Object-Oriented Programming.

    Each component of the Higher-Lower game is broken down into their seperate classes that have a singular responsibility, in line with OOP and SOLID principles.

    Test files for Card, Player and Deck classes were also developed to ensure each class functions as intended.

Ideas for Improvement:
    - Implementing a GUI
    - Additonal Card Games (Fish, BlackJack etc.)
    - Player Perks/Power Moves

Game Overview:
    Each Player starts with 3 points. Players take turns in guessing whether the next card's value is higher or lower than the current card that was drawn. Players gain a point for correct guesses and lose a point for guessing incorrectly.

    Players are eliminated if they reach 0 points or if they draw a Joker.

    Last Player Standing Wins

*INSTRUCTIONS ON RUNNING THE GAME AND TESTS*

To play the game, Run main.py in any IDE that supports a Python Environment:
    - Your_Local_Path\higher-lower-game> python .\main.py

To run the all Unit Tests:
    - python -m pytest