# Count frequency of each word in a sentence.

sentence= "python is easy python is powerful python"

words=sentence.lower().split()
freq={}

for word in words:
    if word==" ":
        continue
    freq[word]=freq.get(word,0)+1

print(freq)

