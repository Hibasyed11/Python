word=input("What is your word? ")
reverse_word=('')
i = len(word)-1
while i >= 0:
    reverse_word += word[i]
    i-=1
if reverse_word == word:
    print(word, "IS a palidrone.")
else:
    print(word, "is NOT a palidrone.")
