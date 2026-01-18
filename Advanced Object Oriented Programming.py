class IOString:
    def __init__(self):
        self.str1=""
    def get_String(self):
        self.str1=input("Enter String: ")
    def print_string(self):
        print("The result of this is", self.str1.upper())
str1=IOString()
str1.get_String()
str1.print_string()

class Employee:
    def __init__(self):
        print('Employee Hired')
    def __del__(self):
        print('Employee Fired')
def Create_obj():
    print('Makin Object...')
    obj=Employee()
    print('function end...')
    return obj
print('Calling Create_obj() function...')
obj=Create_obj()
print('Program End...')

class Pair_Elements:
    def Two_Set(self, nums, target):
        lookup={}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return(lookup[target-num], i)
            lookup[num]=i
value=int(input("Enter the sum you want to find: "))
print("index1=%d, index2=%d" % Pair_Elements() .Two_Set((10,20,30,40,50,60,70), value))