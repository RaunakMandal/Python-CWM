def fizz_buzz(input):
    s = ""
    if input % 3 == 0:
        s += "Fizz"
    if input % 5 == 0:
        s += "Buzz"
    if len(s) == 0:
        s += str(input)
    return s


for i in range(1, 100):
    print(fizz_buzz(i))
