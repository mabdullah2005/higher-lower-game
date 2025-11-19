# Name: Player
# Description:
#   Holds all logic of a singular player

class Person:
    def __init__(self, name: str):
        if len(name == 0):
            raise ValueError("Name Must be a Non-Empty String")
        else:
            self._name = name
            self._score = 5
    
    def increment(self):
        self._score += 1
    
    def decrement(self):
        if(self._score > 0):
            self._score -= 1
    
    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score

    def __str__(self):
        return f'Player: {self._name}, Score: {self._score}'