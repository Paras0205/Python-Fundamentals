#Merge two dict

def merge_two_dicts(d1,d2):

    new_dict=d1.copy()

    new_dict.update(d2)

    return new_dict


d1={"A":10,"B":20}

d2={"B":50,"C":30}

print(merge_two_dicts(d1,d2))