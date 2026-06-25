#Reverse the words in a sentence (keep words, change their order).

# sentence=input("Enter a sentence:")
# words=sentence.split()
# words.reverse()
# print("Reversed sentence:", " ".join(words))

sentence = input("Enter a sentence: ")

words = []
word = ""

for ch in sentence:
    if ch != " ":
        word += ch
    else:
        words.append(word)
        word = ""
words.append(word)

for i in range(len(words) - 1, -1, -1):
    print(words[i], end=" ")
