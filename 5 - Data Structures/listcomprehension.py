# [expression for variable in list]

items = [
    ("Product1", 10),
    ("Product2 ", 5),
    ("Product3 ", 34),
    ("Product4 ", 11),
    ("Product5 ", 56),
]

prices = [item[1] for item in items]
print(prices)

filtered = [item for item in items if item[1] >= 20]
print(filtered)
