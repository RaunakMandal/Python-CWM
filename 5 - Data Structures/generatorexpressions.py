from sys import getsizeof

values = (x * 2 for x in range(10000))
print("Gen Size: ", getsizeof(values), "bytes")
print(values)

for x in values:
    print(x)


vals = [x * 2 for x in range(10000)]
print("List Size: ", getsizeof(vals), "bytes")
