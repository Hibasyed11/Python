class fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color
apple=fruit("apple", "green")
banana=fruit("banana","yellow")
print(apple.name)
print(banana.color)

class student:
    grade=10
    print("Hi, I'm a student in grade", grade)
ob=student()

class vehcile:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
modelX=vehcile(240, 12) 
print("modelX max speed:", modelX.max_speed)
print("modelX mileage:", modelX.mileage)
model2X=vehcile(320,21)
print("model2X max speed:", model2X.max_speed)
print("model2X mileage:", model2X.mileage)

class parrot:
    species="bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
blu=parrot('Blu', 5)
woo=parrot('Woo', 7)
print("{0}'s age is {1}".format(blu.name, blu.age))
print("{0}'s age is {1}".format(woo.name, woo.age))