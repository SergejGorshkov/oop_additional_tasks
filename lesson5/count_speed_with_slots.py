import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_set_del(self):
        self.x = 1
        for self.x in range(100):
            self.x += 1
            del self.y
            self.y = 0

class PointSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_set_del(self):
        self.x = 1
        for self.x in range(100):
            self.x += 1
            del self.y
            self.y = 0

pt = Point(10, 20)        # Без __slots__
pts = PointSlots(10, 20)  # Со __slots__



t1 = timeit.timeit(pt.get_set_del)   # Без __slots__
t2 = timeit.timeit(pts.get_set_del)  # Со __slots__

print(t1, t2)
print((t1-t2)/t1*100)

from sys import getsizeof
print(getsizeof(pt))  # 48 байт в памяти
print(getsizeof(pts))  # 48 байт в памяти
