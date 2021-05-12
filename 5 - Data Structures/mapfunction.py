items = [
    ("Product1", 10),
    ("Product2 ", 5),
    ("Product3 ", 34),
    ("Product4 ", 11),
    ("Product5 ", 56),
]

x = map(lambda item: item[1], items)  # map(function, iterable)
for item in x:
    print(item)

x = list(map(lambda item: item[1], items))
print(x)
