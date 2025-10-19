def sum_of_digits(x):
    '''This recusion function is to find the sum of the digits in a number'''
    if x==0:
        return 0
    else:
        return (x%10)+sum_of_digits(x//10) #use the formula x___(x-1) for factorial and sum of numbers
print (sum_of_digits(1234))
print (sum_of_digits(928))
print (sum_of_digits(1438))

def reverse(s):
    '''This recursive function returns the reverse of a string '''
    if len(s)==0:
        return s
    else:
        return reverse(s[1:])+ s[0]
print(reverse("hello"))
print(reverse("everyone"))
print(reverse("Racecar"))
print(reverse("dream"))