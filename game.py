class Game:
    def guess(self, param):
        if param is None:
            raise TypeError("None은 사용 할 수 없습니다.")