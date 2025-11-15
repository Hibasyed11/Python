def matching_words(words):
    count=0
    Lst=[]
    for word in words:
        if len(word)>2 and word[0]==word[-1]:
            count+=1
            Lst.append(word)
    print("The words in the Lst are:", Lst)
    return count
count=matching_words(["abc", "vc", "cac", 1221, "aba", "zyx"])
print("The count of the numbers is:", count)

L=[4,5,6,2,45,125,10,8]
print("The original list is:", L)
sum=0
for i in L:
    sum+=i
average=sum/len(L)
print("Sum=",sum)
print("Average=",average)
L.sort()
print("The largest number in the list is", L[-1])
print("The smallest number in the list is", L[0])

numbers=[2,5,48,3,15,13,42,8,16]
even_list=[]
odd_list=[]
for i in numbers:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("The even numbers in the list are", even_list)
print("The odd numbers in the list are", odd_list)