# Tasks:
# Remove invalid values (None, "", negative)
# Find total & average

data = [100, None, 200, "", -50, 300]

total=0
count=0
valid_data=[]

for n in data:
    if n==None or n=="":
        continue
    if n<0:
        continue
    valid_data.append(n)
    total+=n
    count+=1

if count>0:
    avg=total/count
else:
    avg=0

print("valid_data:",valid_data)
print("total:",total)
print("avg:",avg)     