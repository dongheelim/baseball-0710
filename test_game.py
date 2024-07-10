from unittest import TestCase

from game import Game


class TestGame(TestCase):
    def test_try_exception_when_input_is_none(self):
        self.game = Game()
        with self.assertRaises(TypeError):
            self.game.guess(None)
