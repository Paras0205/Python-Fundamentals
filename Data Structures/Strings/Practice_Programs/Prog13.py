#WAP TO PRINT ALL OF THE COUNTING OF LETTER IN A STRING AND STORE IN DICTIONARY

s="my name is paras"

dict={}

for char in s:
    if char in dict:
        dict[char]+=1
    else:
        dict[char]=1
print(dict)