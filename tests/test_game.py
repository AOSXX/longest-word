from longest_word.game import Game
import string
#import requests

class TestGame:
    def test_game_initialization(self):
            # setup
            new_game = Game()

            # exercise
            grid = new_game.grid

            # verify
            assert type(grid) == list
            assert len(grid) == 9

            for letter in grid:
                assert letter in string.ascii_uppercase

    def test_is_working(self):
        new_game = Game()
        new_game.grid = list("OQUWRBAZE")

        assert new_game.is_valid("BAROQUE") is True
        assert new_game.is_valid("PIKACHU") is False

    def test_word_is_empty(self):
        new_game = Game()

        assert new_game.is_valid('') is False

    def test_unknown_word_is_invalid(self):
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:

        assert new_game.is_valid('FEUN') is False
