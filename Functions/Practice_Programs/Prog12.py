# clean_names(names)
# Input: list of raw names like [" Paras ", "ravi", "NEHA "].
# Output: list of cleaned names

def clean_names(names):

    clean=[]

    for name in names:
        clean.append(name.strip().lower())

    return clean

names=[" Paras ","ravi","NEHA "]

print(clean_names(names))