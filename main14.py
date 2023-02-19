class Clock:
    __DAY = 86400  # число секунд в одном дне

    def __init__(self, second: int):
        if not isinstance(second, int):
            raise TypeError("Секунды должны быть целым числом")
        self.second = second % self.__DAY

    def get_time(self):  # часы:минуты:секунды
        s = self.second % 60
        m = (self.second // 60) % 60
        h = (self.second // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod  # формат времени
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')

    def __add__(self, other):  # увеличение времени с оперендом справа
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")

        sc = other
        if isinstance(other, Clock):
            sc = other.second

        return Clock(self.second + sc)

    def __radd__(self, other):  # увеличение времени с оперендом слева
        return self + other

    def __iadd__(self, other):  # увеличение времени с +=
        print('__iadd__')
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть типом int или объектом Clock")

        sc = other
        if isinstance(other, Clock):
            sc = other.second

        self.second += sc
        return self


    def __sub__(self, other):  # уменьшение времени с оперендом справа
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")

        sc = other
        if isinstance(other, Clock):
            sc = other.second

        return Clock(self.second - sc)

    def __rsub__(self, other):  # уменьшение времени с оперендом слева
        return self - other

    def __isub__(self, other):  # уменьшение времени с -=
        print('__isub__')
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть типом int или объектом Clock")

        sc = other
        if isinstance(other, Clock):
            sc = other.second

        self.second -= sc
        return self


c1 = Clock(1000)
c2 = Clock(2000)
c3 = Clock(3000)
c4 = 100 + c1 + c2 - c3
c4 += 1000
print(c4.get_time())