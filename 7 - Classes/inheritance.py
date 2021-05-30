# DRY: Don't repeat yourself
# Animal: Parent, Base
# Mammal : Child, Sub

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def eat(self):
        print("eat")

    def walk(self):
        print("walk")


class Fish(Animal):
    def walk(self):
        print("swim")


aa = Fish()
print(aa.walk())
