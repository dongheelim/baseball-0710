class Game:
    def guess(self, number):
        if number is None:
            raise TypeError("None은 사용 할 수 없습니다.")