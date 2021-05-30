# Every class inhertis from Object class
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def eat(self):
        print("eat")


aa = Mammal()
print(isinstance(aa, Animal))
print(isinstance(aa, object))
print(issubclass(Mammal, object))
