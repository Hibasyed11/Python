num=int(input("Input a number. "))
sum=0
temp=num
while temp>0:
    digit= temp % 10
    sum += digit ** len(str(num))
    temp //= 10
if sum==num:
    print("This number IS an Armstrong Number.")
else:
    print("This number is NOT an Armstrong Number.")
