class Point:
    def draw(self):
        print("Draw")


point = Point()
print(type(point))
print(isinstance(point,Point))


#Problem-1
class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    
    def speak(self):
        print(f"Hi this is {self.name} and i am {self.age} old.")

human = Human("John",20)
human.speak()