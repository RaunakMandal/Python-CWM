# One line anonymous functions to pass to another functions

items = [
    ("Product1", 10),
    ("Product2 ", 5),
    ("Product3 ", 34),
    ("Product4 ", 11),
    ("Product5 ", 56),
]

items.sort(key=lambda item: item[1])  # lambda parameters: expressions
print(items)
