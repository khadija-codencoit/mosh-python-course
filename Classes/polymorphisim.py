from abc import ABC,abstractmethod

class UIControl(ABC):
    def draw(self):
        pass

class TexBox(UIControl):
    def draw(self):
        print("TexBox")

class DropBox(UIControl):
    def draw(self):
        print("DropBox")

ddl = DropBox()
print(isinstance(ddl,UIControl))