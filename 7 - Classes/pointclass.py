# first letter is uppercase
class Point:
    def draw(self):  # class must have a var, i.e self
        print("Draw")


point = Point()
point.draw()
print(type(point))
print(isinstance(point, Point))
