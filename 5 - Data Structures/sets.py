# Unordered collection of unique objects

nums = [1, 1, 1, 2, 2, 3, 4, 5, 6, 6, 7]
uniques = set(nums)
print(uniques)

second = {1, 1, 4}
second.add(5)
print(second)
second.remove(4)
print(second)
print(len(second))
