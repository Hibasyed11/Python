try:
    balance=5000
    amount=float(input("What is the amount you wish it take out? "))
    if amount > balance:
        raise Exception ("withdrawal amount exceeds available balence")
    balance -= amount
    print("withdrawal sucessful, remaining balance is", balance)
except ValueError:
    print("Please enter a valid numerical value.")
except Exception as ex:
    print("Transaction Failed,", ex)
finally:
    print("Transaction complteted")

try:
    celsius=float(input("What is the temperature? "))
    fahrenheit=(celsius * 9/5) + 32 
    print("The temperature is", fahrenheit, "degrees fahrenheit.")
except ValueError:
    print("Please input a numerical value.")
finally:
    print("It has been finished")

try:
    stock={"T-shirts":5, "Shoes":2, "Watches":0}
    print("Available Items:",stock)
    item=input("Enter the item you want to buy. ")
    if item not in stock:
        raise Exception ("Item not Found")
    quantity=int(input("How much do you want to buy? "))
    if quantity>stock [item]:
        raise Exception ("Not enough stock")
    print("You have bought", quantity, "number of", item)
except ValueError:
    print("Please enter an acceptable numerical value")
except Exception as x:
    print(x)
finally:
    print("You have sucessfully bought", item)