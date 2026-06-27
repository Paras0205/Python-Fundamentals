# Count frequency of each character in a string.

str="Hello my name is Paras"

freq={}

for char in str:
    if char==" ":
        continue
    freq[char]=freq.get(char,0)+1

for char, count in freq.items():
    print(f"{char} : {count}")