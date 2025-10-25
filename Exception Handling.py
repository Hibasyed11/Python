try:
    num1,num2 = eval(input("Enter 2 number seperated by a comma. "))
    result = num1/num2
except ZeroDivisionError:
    print("Division by zero resulted in an error.")
except SyntaxError:
    print("Enter the numbers seperated by a comma. Like 1,2")
except:
    print("Wrong Input") 
else:
    print("No exceptions")
finally:
    print("This progam will be executed no matter what")