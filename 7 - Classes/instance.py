class Point:
    default_color = "red"  # shared across all objects

    def __init__(self, x, y):  # Self is reference to current object
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_color = "white"
point = Point(1, 3)
print(point.default_color)
print(Point.default_color)
point.draw()

new = Point(1, 6)
new.draw()
