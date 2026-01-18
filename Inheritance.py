class dad:
    def __init__(self, eyes, aggressive):
        self.eyes=eyes
        self.aggresive=aggressive
    def display(self):
        print("Your eye color is", self.eyes)
        print("You are aggressive", self.aggresive)
class son(dad):
    def __init__(self, name, age, eyes, aggressive):
        self.name=name
        self.age=age
        dad.__init__(self, eyes, aggressive)
obj=son("Penguin", 8, 'blue', True)
obj.display()

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class Bus(Vehicle):
    pass
obj=Bus("School Bus", 80, 240)
print("Vehicle Name: ",obj.name,", Max Speed: ",obj.max_speed,", Mileage: ",obj.mileage)

class Person:
    def __init__(self, name, id_number):
        self.name=name
        self.id_number=id_number
    def display(self):
        print(self.name)
        print(self.id_number)
class Employee(Person):
    def __init__(self, name, id_number, salary, post):
        self.salary=salary
        self.post=post
        Person.__init__(self, name, id_number)
a=Employee("Rahul", 26801, 200000, "Intern")
a.display()