from game_result import GameResult


class Game:
    def __init__(self):
        super().__init__()
        self.question = ""

    def guess(self, number):
        self.assert_illegal_value(number)

        if number == self.question:
            return GameResult(True, 3, 0)
        else:
            strikes = 0
            balls = 0
            for idx, q_number in enumerate(self.question):
                strikes += int(number[idx]==q_number)

            for idx, q_number in enumerate(self.question):
                balls += int(number[idx]!=q_number and q_number in number)

            return GameResult(False, strikes  , balls)

    def assert_illegal_value(self, number):
        if number is None:
            raise TypeError("None은 사용 할 수 없습니다.")
        if len(number) != 3:
            raise TypeError("자릿수가 3자리 이어야 합니다.")
        if not all(ord("0") <= ord(char) <= ord("9") for char in number):
            raise TypeError()
        if self.is_duplicated(number):
            raise TypeError()

    def is_duplicated(self, number):
        return len(set(number)) != 3
