#List comprehensions are just a short way to build a new list from an existing sequence,
#using a loop and optional condition in a single line.

# Think of them as:
    # “For each item in something, produce this expression, maybe only if a condition is true.”

marks = [85, 42, 91, 60, 38, 75]

# Old way — loop + append
passed = []
for m in marks:
    if m >= 50:
        passed.append(m)

# New way — list comprehension (same result, one line)
passed = [m for m in marks if m >= 50]
print(passed)            # [85, 91, 60, 75]

# Transform values
doubled = [m * 2 for m in marks]
names   = ["paras", "rahul", "priya"]
clean   = [n.title() for n in names]


#  Common patterns
# a) Transform each item

# Double each value:
nums = [1, 2, 3, 4]
doubles = [n * 2 for n in nums]

# Uppercase all words:
words = ["data", "python", "pandas"]
upper_words = [w.upper() for w in words]


# b) Filter items

# Keep words containing "a":
fruits = ["apple", "banana", "kiwi", "mango"]
with_a = [f for f in fruits if "a" in f]

# Keep numbers greater than 10:
nums = [5, 12, 3, 18]
big = [n for n in nums if n > 10]

# c) Extract part of each item

# First character of each word:
words = ["data", "python", "analyst"]
first_chars = [w[0] for w in words]

# Lengths of words:
words = ["data", "python", "analyst"]
lengths = [len(w) for w in words]