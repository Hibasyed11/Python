choice=input("Choose square or cube. ")
num=int(input("Input a number. "))
def power_tool(num,choice):
    if choice=="square":
        return num**2
    elif choice=="cube":
        return num**3
    else:
        print("Incorect input,please try again.")
print(power_tool(num,choice))

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print("Please select the operation...")
print("a=addition")
print("b=subtract")
print("c=multiply")
print("d=divide")
choice=input("Selected=")
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
if choice=="a":
    print("The solution is", (add(num1,num2)))
elif choice=="b":
    print("The solution is", (subtract(num1,num2)))
elif choice=="c":
    print("The solution is", (multiply(num1,num2)))
elif choice=="d":
    print("The solution is", (divide(num1,num2)))
else:
    print("Wrong input,try again")