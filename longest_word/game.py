# pylint: disable=missing-module-docstring
# pylint: disable=too-few-public-methods
import random
import string


class Game:
    """Game is a class to play the matching word game"""
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = [random.choice(string.ascii_uppercase) for i in range(9)]

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        temp = self.grid
        if not word:
            return False
        for i in word:
            match = False
            for index,j in enumerate(temp):
                if i == j:
                    temp.pop(index)
                    match = True
                    break
            if match is False:
                return False


        return True
