# count_chars(text)
# Input: a string.
# Output: a dict of character → count.

def count_chars(text):

    freq={}

    for char in text:
        if char!=" ":
            freq[char]=freq.get(char,0)+1
    return freq

print(count_chars("Hello"))