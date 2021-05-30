class Point:
    def __init__(self, x, y):  # initialization
        self.x = x
        self.y = y

    def __eq__(self, other):  # equality
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):  # greater
        return self if self.x > other.x and self.y > other.y else other

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 6)
point_2 = Point(5, 3)
print((point > point_2).draw())
