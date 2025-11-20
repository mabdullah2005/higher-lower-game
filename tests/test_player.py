import pytest
from game.Player import Player

def test_player_empty_name():
    with pytest.raises(ValueError) as error:
        Player("")
    
    assert str(error.value) == "Player Must Have a Name"

def test_player_string_at_start():
    player = Player("Abdullah")

    assert str(player) == "Player: Abdullah (Alive), Score: 5"

def test_player_string_when_eliminated():
    player = Player("Abdullah")
    while(player.is_alive()):
        player.decrement()

    assert str(player) == "Player: Abdullah (Eliminated), Score: 0"

def test_player_string_when_score_incremented():
    player = Player("Abdullah")
    player.increment()

    assert str(player) == "Player: Abdullah (Alive), Score: 6"

def test_player_string_when_score_decremented():
    player = Player("Abdullah")
    player.decrement()

    assert str(player) == "Player: Abdullah (Alive), Score: 4"