#Pop item, Pop, Clear, and Delete
squares={1:1, 2:4,3:9, 4:16, 5:25}
print(squares.pop(4))
print(squares)
print(squares.popitem())
print(squares)
squares.clear()
print(squares)
del squares

#The Count of Something
test_dic={'python':2, 'is':2, 'the':2, 'best':2, 'for':2, 'coding':1}
k=2
count=0
for key in test_dic:
    if test_dic[key]==k:
        count+=1
print("The number of 2s in the dictionary is", count)

#Printing Something from the Code
country_code={'India':'0091', 'Australia':'0025', 'Nepal':'00977'}
print("The counstry code for India is:")
print(country_code.get('India', 'Not Found'))
print("The counstry code for Japan is:")
print(country_code.get('Japan', 'Not Found'))

#Find the Highest Value
marks={'Maths':88, 'English':92, 'Science':96, 'Hisory':74}
top_score=max(marks, key=marks.get)
print("The highest scoring subject is", top_score)

#Reversing Dictionary and Interchanging
student={'Name':'Arjun', 'Age':12, 'Grade':'6A'}
reversed_dic={}
for key, value in student.items():
    reversed_dic[value]=key
print(reversed_dic)  
student1={'Place':'USA', 'Age':121}
student.update(student1)
print(student)  

#Coverting a List to a Dictionary
keys=['Name', 'Age', 'City']
values=['Rohan', 12, 'Delhi']
result=dict(zip(keys, values))
print(result)