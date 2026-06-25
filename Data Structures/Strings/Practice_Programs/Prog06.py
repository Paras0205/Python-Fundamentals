#Capitalize the first letter of each word in a sentence.

sen=input("enter a sentence:")

words=[]
word=""

for char in sen:
    if char!="":
        word+=char
    else:
        words.append(word)
        word = ""
words.append(word)

for word in words:
    print(word.title(), end=" ")