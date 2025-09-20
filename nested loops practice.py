lower= int(input("Input your lower number. "))
upper= int(input("Input your higher number. "))
for i in range (lower,upper+1):
    if i>1:
        for j in range (2,i):
            if i%j==0:
                break
        else:
            print(i)


for i in range (1,6):
    for j in range (1,11):
        print(i,"x",j,"=", i*j)
    print()


for i in range (1,6):
    for j in range (1,i+1):
        print(j,end="")
    print()

    i=1
while i<=10:
    j=1
    while j<=10:
        print("{0} x {1} = {2}".format(i,j,i*j))
        j+=1
    i+=1    
    print('')