class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"{self.name} and {self.age}")


person = Person("kk",16)
person.display()

#problem-1

class Teamperature:
    def __init__(self,celsius):
        self.celsius = celsius

    def __str__(self):
        return f"{self.celsius}°C" 
       

    def __eq__(self, value):
        return self.celsius == value

temp = Teamperature(25)

print(temp)
print(temp == 25)    
print(temp == 30)   