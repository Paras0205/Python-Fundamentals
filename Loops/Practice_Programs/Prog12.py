# Keep taking input from user until they enter 0.
# Then print total and average.
total = 0
count = 0
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    total += num
    count += 1
if count > 0:
    average = total / count
    print("Total:", total)
    print("Average:", average)
else:
    print("No numbers entered.")