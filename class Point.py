from math import hypot
class Point:
    def __init__(self,x:float=0,y:float=0)->None:
        self.move(x,y)

    def move(self,x:float,y:float)->None:
        self.x=x
        self.y=y
    def reset(self):
        self.move(0,0)
    def faseleh(self,other):
        return hypot(self.x-other.x,self.y-other.y)


p1 = Point()
p2 = Point()
p3 = Point()
p4 = Point(10,12)
print(20*"-","p1",20*"-")
print(p1.x)
print(p1.y)
print(20*"-","P2",20*"-")
print(p2.x)
print(p2.y)
print(20*"-","P3",20*"-")
print(p3.x)
print(p3.y)
print(20*"-","P4",20*"-")
print(p4.x)
print(p4.y)
print(p4.faseleh(p1))