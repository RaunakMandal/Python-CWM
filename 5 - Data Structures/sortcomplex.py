items = [
    ("Product1", 10),
    ("Product2 ", 5),
    ("Product3 ", 34),
    ("Product4 ", 11),
    ("Product5 ", 56),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
