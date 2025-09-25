class Animal:
    def __init__(self,age):
        self.age = age

    def eat(self):
        print("eat")

class Mammal(Animal):
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal(4)
m.eat()