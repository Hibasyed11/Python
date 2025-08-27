amount=327
note_1=(amount//100)
note_2=(amount%100//50)
note_3=(amount%100%50//10)
amountleft=(amount%100%50%10)
print("There will be", note_1, "100 dollar notes")
print("There will be", note_2, "50 dollar notes")
print("There will be", note_3, "10 dollar notes")
print("There will be", amountleft, "1 dollar notes\n")

number1=32
number2=90
number3=63
number4=27
sumofnumbers=(number1+number2+number3+number4)
print("The sum of the numbers is", sumofnumbers)
average=(sumofnumbers/4)
print("The average of the numbers is", average)