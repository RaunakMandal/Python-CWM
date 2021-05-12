try:
    with open("hehe.py") as file:
        print("File opened")
except Exception as e:
    print(e)
else:
    print("NO exceptions")
