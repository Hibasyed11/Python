rowSize=int(input("What is your row size. "))
if rowSize%2==0:
    half_DimondRow=rowSize//2
else:
    half_DimondRow=rowSize//2+1

for i in range (1, half_DimondRow+1):
    spaces=" "*(half_DimondRow-i)
    numbers=""
    for x in range (1,2*i):
        numbers= numbers +str(x)
    print(spaces+numbers) 

for i in range (1, half_DimondRow):
    spaces=" "*i
    numbers=""
    for x in range (1,2*(half_DimondRow-i)):
        numbers= numbers+str(x)
    print(spaces + numbers)