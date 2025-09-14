for i in range (5):
    for j in range (1,11):
        print(j,end=(""))
        j+=1
    i+=1
    print("")


string=input("Input a string. ")
char=input("Input a character you want to find. ") 
i=0
count=0
while i<len(string):
    if string[i] == char:
        count= count+1
    i+=1
print("There are {0} {1}'s in the string.".format(count,char))


for i in range (1,11):
    for j in range(1,11):
        print(i*j,end="\t")
    print('')
