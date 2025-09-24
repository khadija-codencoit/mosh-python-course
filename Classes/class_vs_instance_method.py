class Point:
    defalut_colour = "red"

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point {self.x} and {self.y}")

    @classmethod
    def zero(cls):
        return cls(0,0)


point = Point(1,3)
point = Point.zero()
point.draw()