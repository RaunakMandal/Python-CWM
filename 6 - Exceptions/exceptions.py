# Exceptions: Terminates execution of program
try:
    age = int(input("Age: "))
except ValueError as e:
    print("You did not enter a valid age")
    print(e)
    print(type(e))
else:
    print("NO exceptions")
print("Execution continues")
