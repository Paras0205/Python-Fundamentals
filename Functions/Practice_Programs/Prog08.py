# word_freq(sentence)
# Input: string sentence.
# Output: dict of word → frequency.

def word_freq(sentence):

    split_sentence=sentence.split()

    freq={}

    for word in split_sentence:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1

    return freq

print(word_freq("Hello my name is Paras"))