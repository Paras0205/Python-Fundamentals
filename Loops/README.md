# Loops in Python

## Overview

Loops are used to execute a block of code repeatedly, reducing code duplication and improving efficiency.

Instead of writing the same code multiple times, loops allow us to automate repetitive tasks.

---

## Topics Covered

### 1. For Loop

Used when the number of iterations is known or when iterating through a sequence such as a list, string, or range.

```python
for i in range(5):
    print(i)
```

### 2. While Loop

Used when repetition should continue until a condition becomes false.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

### 3. Break Statement

Terminates the loop immediately when a specific condition is met.

```python
for i in range(1, 11):
    if i == 5:
        break
    print(i)
```

### 4. Continue Statement

Skips the current iteration and moves to the next iteration.

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

### 5. Nested Loops

A loop inside another loop.

```python
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)
```

---

## Important Loop Patterns

### Accumulator Pattern

Used to calculate totals or sums.

```python
total = 0
for x in data:
    total += x
```

### Counter Pattern

Used to count items matching a condition.

```python
count = 0
for x in data:
    if x > 100:
        count += 1
```

### Filter Pattern

Used to select or display specific items.

```python
for x in data:
    if x > 100:
        print(x)
```

### Search Pattern

Used to find whether a particular value exists.

```python
found = False

for x in data:
    if x == target:
        found = True
```

---

## Learning Outcomes

After completing this module, I learned:

* How to use `for` and `while` loops
* When to use `break` and `continue`
* How nested loops work
* Common loop patterns used in Data Analytics and Programming
* Writing cleaner and more efficient code using loops

---

**Author:** Paras
