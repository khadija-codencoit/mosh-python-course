class Employee:
    def greet(self):
        print("Hello Employee")

class Person:
    def greet(self):
        print("Hello Person")

class Manager(Person,Employee):
    pass

manager = Manager()
manager.greet()