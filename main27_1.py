class Point2D:
    __slots__ = ('x', 'y', '__lenght')
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__lenght = (x * x + y * y) ** 0.5

    @property
    def lenght(self):
        return self.__lenght

    @lenght.setter
    def lenght(self, value):
        self.__lenght = value
