class Person:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight

    def setAge(self, age):
        self.age= age
        print("hello my name is " + self.name)
    def getAge(self):
        return self.age;


rohitObj= Person("rohit")
rohitObj.setAge(27)
print(rohitObj.getAge());#27
rohitObj.getWeight()#weight not available
rohitObj.setWeight(56);
rohitObj.name = 'rohit1' #error. because name is private





myclass.myfunc()
print(myclass.weight)
myclass.age=29
print(myclass.age)
