import pytest
from game.Player import Player

# Tests that a Player Object with an empty name parameter is not accepted
def test_player_empty_name():
    with pytest.raises(ValueError) as error:
        Player("")
    
    assert str(error.value) == "Player Must Have a Name"

# Tests that a valid Player Object is correctly constructed
def test_player_string_at_start():
    player = Player("Abdullah")

    assert str(player) == "Player: Abdullah (Alive), Score: 5"

# Tests that an eliminated player is correctly displayed
def test_player_string_when_eliminated():
    player = Player("Abdullah")
    while(player.check_alive()):
        player.decrement()

    assert str(player) == "Player: Abdullah (Eliminated), Score: 0"

# Tests that a player is correctly displayed after their score is increased
def test_player_string_when_score_incremented():
    player = Player("Abdullah")
    player.increment()

    assert str(player) == "Player: Abdullah (Alive), Score: 6"

# Tests that a player is correctly displayed after their score has been decreased
def test_player_string_when_score_decremented():
    player = Player("Abdullah")
    player.decrement()

    assert str(player) == "Player: Abdullah (Alive), Score: 4"