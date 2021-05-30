class Point:
    def __init__(self, x, y):  # initialization
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 6)
point_2 = Point(5, 3)
print((point + point_2).draw())
