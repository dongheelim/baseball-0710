class Game:
    def guess(self, number):
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