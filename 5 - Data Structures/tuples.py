# Immutable => can't change data

point = (1, 2) + (3, 4)
print(point)
point = (1, 2) * 10
print(point)
point = tuple("Hello World")
print(point)

# point[0] = 150 # Error
