#List Comprehension
numbers=[1,2,3,4,5,6,7,8]
even=[x for x in numbers if x%2==0 ]
print(even)

#Dictionary Comprehension
my_dic={str(x): x**2 for x in [1,2,3,4,5]}
print("\n", my_dic)

#Maps Function
def squares(n):
    return n*n
numbers=[1,2,3,4,5]
result=map(squares, numbers)
print("\n", list(result))

#Zip Function
name=["Zunairah", "Humairah", "Hiba", "Zubair"]
roll_number=[4,1,8,3]
result=list(zip(name, roll_number))
print("\n", result)

#Exit Function
ages=[19,45,12,24]
print("\n")
for age in ages:
    if age<18:
        print(age," is not allowed")
        print(exit)
        exit()
    else:
        print(age, "is allowed")