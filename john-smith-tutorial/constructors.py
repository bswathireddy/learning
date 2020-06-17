#__init is the short cut for initialization
class Point:
    def __init__(self,x,y):#used to construct object and initialize values
        self.x=x
        self.y=y
    def  move(self):
        print(move)
    def draw(self):
        print(draw)


point=Point(2,3)
point.x=4
print(point.x)