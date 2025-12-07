number1=[1,2,3]
number2=[4,5,6]
result=map(lambda x,y:x+y, number1, number2)
print(list(result))

num=[6,7,8,9,10]
def sq(n):
    return n*n
squares=list(map(sq,num))
print(squares)

s1={2,1,3}
s2={'a', 'b', 'c'}
s3=list(zip(s1,s2))
print(s3)

list1=[100,200,300]
list2=[150,250,350]
list3=list(zip(list1,list2[::-1]))
print(list3)

stocks=['reliance', 'infosys', 'tcs']
prices=[2589, 1348, 4203]
result={stocks:prices for stocks,prices in zip(stocks,prices)} 
print(result)

for i in range (1,11):
    if i==5:
        print(exit)
        exit()
    print(i)