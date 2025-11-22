tuplex=("Hi",True, 3.2, 1)
print(tuplex)
tuplex=(2,5,4,10,13)
print(tuplex)
tuplex=("Jump", "From", "Earth")
print(tuplex)
tuplex=tuplex+(9,)
print(tuplex)

numbers=(50,10,60,70,50)
count=numbers.count(50)
print(count)

indexing=(2,4,8,6,2,5,10,3,9,7)
slicing=indexing[3:5]
print(slicing)

def palind(r):
    e=len(r)-1
    s=0
    while (s<e):
        if (r[s]!= r[e]):
            return False
        s+=1
        e-=1
    return True
r=(1,2,3,3,2,1) 
if (palind(r)):
    print("This is a palidrone")
else:
    print("This is not a palidrone")

weather=(1,0,0,0,1,1,0)
sunny=0
rainy=0
for i in weather:
    if weather[i]==0:
        rainy+=1
    else:
        sunny+=1
if rainy>sunny:
    print("It is going to rain tommorow")
else:
    print("It is going to be sunny tommorow")