# Conditional Statements in Python

## Overview

Conditional statements allow a program to make decisions based on certain conditions. They help control the flow of execution by running different blocks of code depending on whether a condition is True or False.

---

## Topics Covered

### 1. if Statement

Executes a block of code if the condition is True.

```python
age = 18

if age >= 18:
    print("Eligible to vote")
```

### 2. if-else Statement

Executes one block if the condition is True and another if it is False.

```python
age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

### 3. if-elif-else Statement

Used when there are multiple conditions to check.

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")
```

### 4. Nested if Statement

An if statement inside another if statement.

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
```

---

## Files Included

* `if-else.py` → Basic if-else programs
* `if-elif-else.py` → Multiple condition examples
* `Nested-if.py` → Nested if statement programs
* `Practice_programs.py` → Practice questions and solutions

---

## Learning Outcomes

After completing this module, I learned:

* How to make decisions using conditional statements
* Difference between if, if-else, and if-elif-else
* How nested if statements work
* Writing logical conditions using comparison and logical operators
* Solving real-world decision-making problems using Python

---

**Author:** Paras
