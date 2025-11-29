#Basic Set Operations:
integers={1,2,3,4,5,6}
print(integers)
mixed={"Hi", 6, True, 4.5}
print(mixed)
repeated={1,2,3,4,3,2,4}
print(repeated)
list_to_set=([1,2,3,2,5])
print(list_to_set)
set={1,2,3}
print(set)
set.pop()
print(set)

#Finding the Intersection Union, Difference, Symmetric Difference:
setx={"green", "blue"}
sety={"blue", "yellow"}
print("The original values of the sets are:")
print(setx)
print(sety)
print("\nThe intersection between the two is...")
setz=setx.intersection(sety)
print(setz)
print("\nThe union between the two is...")
setza=setx.union(sety)
print(setza)
print("\nThe difference between the two is...")
setzb=setx-sety
print(setzb)
print("\nThe symmetric difference between the two is...")
setzc=setx.symmetric_difference(sety)
print(setzc)

#Operations with Array
import array as arr
array_num=arr.array('i', [1,3,5,3,7,9,3])
print("\nThe original array: "+str(array_num))
print("The number of occurrences of the 3 in the array is: "+str(array_num.count(3)))
array_num.reverse()
print("The reverse of the order of the array is:")
print(str(array_num))