# Unordered collection of unique objects

nums = [1, 1, 2, 3, 4]
first = set(nums)
sec = {1, 5}

print(first | sec)  # Union
print(first & sec)  # Intersection
print(first - sec)  # Difference
print(first ^ sec)  # Symmetric Difference -> either first and second but not both
