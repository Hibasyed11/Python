lower=int(input("Enter your lower range. "))
upper=int(input("Enter your upper range. "))
num=lower
while num <= upper:
    i=2
    is_prime=True
    if num>1:
        while i<num:
            if num%i==0:
                is_prime=False
                break
            i+=1
        if is_prime:
            print(num)    
    num+=1        
