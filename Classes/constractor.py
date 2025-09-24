class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def drew(self):
        print(f"Point {self.x} and {self.y}")

point = Point(1,22)
point.drew()