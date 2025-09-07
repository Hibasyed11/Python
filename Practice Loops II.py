num=int(input("Input a number. "))
i = 2
is_prime = True
while i < num:
    if num % i==0:
        is_prime = False
        break
    i+=1

if is_prime == True:
    print("This is a prime number.") 
else:
    print("This is not a prime number.") 

num=int(input("Input a list of numbers. "))
even_numbers=0
odd_numbers=0
while num > 0:
    digit = num % 10
    if digit % 2==0:
        even_numbers+=1
    else:
        odd_numbers+=1
    num//=10
print("\nThere are", even_numbers ,"even numbers, and", odd_numbers ,"odd numbers")