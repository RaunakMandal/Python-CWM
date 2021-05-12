numbers = list(range(5))
numbers = [*range(5), *"Hello"]
print(numbers)


first = [1, 2]
second = [3]
vals = [*first, "a", *second, *"Hello"]
print(vals)


dict1 = {"A": 1, "B": 2}
dict2 = {"X": 15}
combined = {**dict1, **dict2, "z": 1}
print(combined)
