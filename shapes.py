import math


class Shape:
    def __init__(self, shape, x=0, y=0):
        self.shape = shape
        self.x = x
        self.y = y

    def square_area(self):
        area = math.pi * self.x ** 2
        return area

    def triangle_are(self):
        pass

