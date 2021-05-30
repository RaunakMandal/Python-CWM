# Use must not use multi level inheritance
class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class ChickeN(Bird):
    def fly(self):
        super().fly()
