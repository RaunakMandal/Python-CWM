items = [
    ("Product1", 10),
    ("Product2 ", 5),
    ("Product3 ", 34),
    ("Product4 ", 11),
    ("Product5 ", 56),
]

x = list(filter(lambda item: item[1] >= 20, items))
print(x)
