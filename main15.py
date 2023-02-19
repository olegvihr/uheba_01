class Clock:
    __DAY = 86400  # число секунд в одном дне

    def __init__(self, second: int):
        if not isinstance(second, int):
            raise TypeError("Секунды должны быть целым числом")
        self.second = second % self.__DAY

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Операнд справа должен иметь тип int или Clock")

        return other if isinstance(other, int) else other.second

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.second == sc

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.second < sc

    def __gt__(self, other):
        sc = self.__verify_data(other)
        return self.second > sc

    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.second <= sc

c1 = Clock(3000)
c2 = Clock(2000)
print(c1 > c2)