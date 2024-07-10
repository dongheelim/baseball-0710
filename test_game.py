from unittest import TestCase

from game import Game


class TestGame(TestCase):
    def test_try_exception_when_invalid_input(self):
        self.assert_illegal_argument(None)
        self.assert_illegal_argument("12")
        self.assert_illegal_argument("1234")

    def assert_illegal_argument(self, guess_number):
        try:
            self.game.guess(guess_number)
            self.fail()
        except TypeError:
            pass

    def setUp(self):
        self.game = Game()
        super().setUp()