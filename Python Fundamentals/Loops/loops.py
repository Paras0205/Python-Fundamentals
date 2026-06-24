# # A loop repeats work so you don’t have to write the same code again and again.
# # For example, instead of printing numbers 1 to 5 manually, you can use a loop.

# # Example:

# # python
# # for i in range(1, 6):
# #     print(i)

# for loop
# Use a for loop when you know how many times you want to repeat something,
# or when you want to go through items in a sequence like a list, string, or range

# for i in range(5):
#     print(i)

# while loop
# Use a while loop when you want repetition to continue until a condition becomes false.

# Example:

# python
# count = 1

# while count <= 5:
#     print(count)
#     count += 1    

# break
# break is used to stop a loop early when a condition is met.

# Example:

# python
# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)

# continue
# continue skips the current iteration and moves to the next one.

# Example:

# python
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

# Nested loops
# A nested loop means one loop inside another.

# Example:

# python
# for i in range(1, 4):
#     for j in range(1, 3):
#         print(i, j)


# Imp loops pattern

# 1.Accumulator Pattern (SUM / TOTAL)
# Used when:
#     You need total
#     You need combined value

# total = 0
# for x in data:
#     total += x   
    
# Key idea:
#     Variable outside loop, update inside loop


# 2.Counter Pattern (COUNT)
# Used when:
#     Counting items that match a condition

# count = 0
# for x in data:
#     if x > 100:
#         count += 1
        

# 3.Filter Pattern (SELECT)
# Used when:
#     Printing or storing specific items

# for x in data:
#     if x > 100:
#         print(x)


# 4.Search Pattern (FIND)
# Used when:
#     Checking if something exists

# found = False
# for x in data:
#     if x == target:
#         found = True