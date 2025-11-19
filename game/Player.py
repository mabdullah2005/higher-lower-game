# Name: Player
# Description:
#   Holds all logic of a singular player

class Player:
    def __init__(self, name: str):
        if len(name) == 0:
            raise ValueError("Player Must Have a Name")
        else:
            self._name = name
            self._score = 5
            self._player_alive = True
    
    def increment(self):
        if(self._player_alive):
            self._score += 1
    
    def decrement(self):
        if(self._score > 0):
            self._score -= 1
    
    def eliminate(self):
        if(self.score == 0):
            self._player_alive = False
        
        return self._player_alive
    
    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score
    
    @property
    def player_status(self):
        if(self._player_alive):
            return "Alive"
        return "Eliminated"

    def __str__(self):
        return f'Player: {self._name} ({self.player_status}), Score: {self._score}'