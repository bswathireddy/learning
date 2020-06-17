class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f"Hi I am {self.name}")


Name=Person("swathi")
Name.talk()

Name2=Person("rohit")
Name2.talk()