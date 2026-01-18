class myClass:
    __privateVar=27
    def __privateMeth(self):
        print("I'm inside class myClass!")
    def hello(self):
        print("Private Variable Value:",myClass.__privateVar)
foo=myClass()
foo.hello()
foo.__privateMeth

class computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print("Selling Price:", self.__maxprice)
    def setMaxPrice(self,price):
        self.__maxprice=price
c=computer()
c.sell()
c.__maxprice=1000
c.sell()
c.setMaxPrice(1000)
c.sell()

class Point:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
p1=Point(2,3)
print(p1)

class Player():
    __health=("Healthy")
    def records(self):
        return self.__health
    def SetHealth(self,health):
        Player.__health=health
p=Player()
print(p.records())
p.__health=("Sick")
print(p.records())
p.SetHealth("Sick")
print(p.records())