# Longest Word in Sentence

sentence = "data science and machine learning"

words=sentence.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)