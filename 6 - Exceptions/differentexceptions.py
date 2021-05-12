try:
    age = int(input("Age: "))
    xfactor = 10 / age
except Exception as e:
    print(e)
else:
    print("NO exceptions")
print("Execution continues")
