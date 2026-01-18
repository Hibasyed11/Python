class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self, other):
        if(self.a<other.a):
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"
    def __eq__(self, other):
        if(self.a==other.a):
            return "ob1 is equal to ob2"
        else:
            return "ob1 is not equal to ob2"
ob1=A(4)
ob2=A(5)
print("Passing Values: ", ob1.a,ob2.a)
print(ob1<ob2)
ob3=A(6)
ob4=A(6)
print("Passing Values: ", ob3.a,ob4.a)
print(ob3==ob4)

class flashcards:
    def __init__(self, word, meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+ "(" +self.meaning+ ")"
flash=[]
print("Welcome to Flashcard Application")
while True:
    word=input("Enter the Word: ")
    meaning=input("Enter your Definition: ")
    x=flashcards(word,meaning)
    flash.append(x)
    option=int(input("Enter 0 if you want to make more flashcards, else enter 1: "))
    if (option):
        break
print("\nYour Flashcards")
for i in flash:
    print(">", i)