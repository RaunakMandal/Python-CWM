class Animal:
    def __init__(self):
        print("animal const")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()  # if it not used it will replace init
        print("mammal const")
        self.weight = 3

    def eat(self):
        print("eat")


aa = Mammal()
print(aa.age)
print(aa.weight)
