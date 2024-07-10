from unittest import TestCase

from game import Game
from game_result import GameResult

class TestGame(TestCase):
    def test_try_exception_when_invalid_input(self):
        self.assert_illegal_argument(None)
        self.assert_illegal_argument("12")
        self.assert_illegal_argument("1234")
        self.assert_illegal_argument("12s")
        self.assert_illegal_argument("111")

    def test_return_solve_result_if_matched_number(self):
        self.game.question = "123"
        result : GameResult = self.game.guess("123")

        self.assertIsNotNone(result)
        self.assertTrue(result.get_solved())
        self.assertEqual(3, result.get_strikes())
        self.assertEqual(0, result.get_balls())

    def assert_illegal_argument(self, guess_number):
        try:
            self.game.guess(guess_number)
            self.fail()
        except TypeError:
            pass

    def setUp(self):
        self.game = Game()
        super().setUp()