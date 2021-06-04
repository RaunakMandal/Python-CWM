# Bad Multiple Inheritance
class Employee:
    def greet(self):
        print("Employee greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):  # this order can ruin things
    pass


manager = Manager()
manager.greet()


# Good Multiple Inheritance
class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass
