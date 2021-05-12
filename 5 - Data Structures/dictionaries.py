# key, value pair
point = {"x": 1, "y": 2, "z": 3}
print(point)

point2 = dict(x=1, y=2)
print(point2["y"])  # keys are indices

# M - 1
if "z" in point:
    print(point["z"])

# M - 2
print(point.get("a", "Not Found"))

del point["x"]
print(point)

for key in point:
    print(key, point[key])

for x in point.items():
    print(x)
