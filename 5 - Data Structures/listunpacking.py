numbers = [1, 2, 3]
first, second, third = numbers  # no of left must be = no of list elements
first, second, *other = numbers  # * holds all leftover items
first, *other, last = numbers
print(first, second, third)
print(other)
