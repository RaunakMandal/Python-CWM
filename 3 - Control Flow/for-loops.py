for number in range(3):  # 0 to range(num)
    print("Attempt", number + 1, (number + 1) * "*")


print("New Loop: ")
for number in range(1, 10):  # ranges from (start, end)
    print("Attempt", number, (number) * "*")

print("New Loop: ")
for number in range(1, 10, 2):  # ranges from (start, end, step) like i++ or i--
    print("Attempt", number, (number) * "*")
