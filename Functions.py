def weather_conditions():
    print("The weather is a little chilly in", spring)
    print("The leaves fall a lot in", autumn)
spring="autumn"
autumn=spring
weather_conditions()

def even(a):
    if a%2==0:
        return True
    else:
        return False
print(even(5))

def sum_of_numbers(a):
    sum=0
    for i in range (1,a+1):
        sum+=i

    return sum
print(sum_of_numbers(4))