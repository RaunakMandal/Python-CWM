import random
import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))
print(random.choices([1, 2, 3, 4], k=2))
print("".join(random.choices("abcedfghijkl", k=5)))

print("".join(random.choices(string.ascii_letters + string.digits + " ", k=12)))
print(random.randbytes(n=5))

nums = [1, 2, 3, 4, 5, 6]
random.shuffle(nums)
print(nums)
