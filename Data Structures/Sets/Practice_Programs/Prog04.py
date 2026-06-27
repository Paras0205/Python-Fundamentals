#WAP TO PRINT ALL COMMON ELEMENT FROM 4 LIST

l1=[2,3,4,6,9,11]
l2=[6,8,3,2,12]
l3=[5,1,15,3,2]
l4=[5,1,2,3,7]
a = set(l1)
b = set(l2)
c = set(l3)
d = set(l4)
my_set=a.intersection(b).intersection(c).intersection(d)
print(my_set)