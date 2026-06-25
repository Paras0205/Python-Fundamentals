# Word Frequency

sentence = "python is easy and python is powerful"

freq={}

words=sentence.split()

for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print(freq)