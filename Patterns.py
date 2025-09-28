rows=int(input("How many rows do you want? "))
for i in range(rows,0,-1):
    indentation=" "*(rows-i)
    row_numbers=[]
    for j in range (i):
        row_numbers.append(str(i))
    number=" ".join(row_numbers)
    print(indentation+number)