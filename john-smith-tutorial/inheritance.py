class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("Dogs bark")


class Cat(Mammal):
    def meow(self):
        print("Cat sounds as meow")


Dog1=Dog()
Dog1.bark()

Cat1=Cat()
Cat1.meow()