# Constructor: special method when called a new object
class Point:
    def __init__(self, x, y):  # Self is reference to current object
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 3)
point.draw()
