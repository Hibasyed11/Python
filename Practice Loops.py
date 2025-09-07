num=int(input("Input your number. "))
reverse_num=0
while num != 0:
    digit= num%10
    reverse_num = reverse_num*10+digit
    num= num//10
print("The reverse number is",reverse_num)

num2=input("Input your number. ")
reverse_num2=('')
i=len(num2)-1
while i>= 0:
    reverse_num2 = reverse_num2 + num2[i]
    i+=-1
print("The reverse number is",reverse_num2)

num3=input("Input your number. ")
reverse_num3=num3[::-1]
print("The reverse number is",reverse_num3)
if num3==reverse_num3:
    print("\nThis number IS a palidrone")
else:
    print("\nThis number is NOT a palidrone")
