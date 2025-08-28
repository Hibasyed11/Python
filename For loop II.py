Lowestnum=int(input("Input the lowest number. "))
Highestnum=int(input("Input the Highest number. "))
for i in range(Lowestnum, Highestnum+1):
    if i%3==0 and i%5==0:
        print(i)