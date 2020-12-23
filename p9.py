'''Problem 1: There are two child classes and one Parent class.'''
'''I called super() class method called act() in child class to print Spam and to make my problem 1 work.'''
class C(object):
    def act(self):
        print("spam")

class D(C):
    def act(self):
        super().act()
        print("eggs")

class E(C):
    def act(self):
        super().act()
        print("ham")

x = D()
x.act()
x=E()
x.act()