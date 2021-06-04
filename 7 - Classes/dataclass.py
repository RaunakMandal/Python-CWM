from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])  # when only data no methods use this
p1 = Point(x=1, y=2)
print(p1.x)
p1 = Point(x=10, y=1)
p2 = Point(x=1, y=2)
print(p1 == p2)
