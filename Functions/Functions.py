# A function is a named block of code that:
# has a name (def my_function),
# can take inputs (parameters),
# can return an output (return),
# can be called many times.

def add(a, b):
    result = a + b
    return result

x = add(3, 5)   # x = 8

# Without function 
# Calculating grade 3 times — repeated code, hard to change
marks1 = 85
if marks1 >= 75: grade1 = "A"
elif marks1 >= 60: grade1 = "B"
else: grade1 = "C"

marks2 = 55
if marks2 >= 75: grade2 = "A"
elif marks2 >= 60: grade2 = "B"
else: grade2 = "C"

# With function 
# Write logic once, use everywhere
def get_grade(marks):
    if marks >= 75: return "A"
    elif marks >= 60: return "B"
    else: return "C"

grade1 = get_grade(85)   # A
grade2 = get_grade(55)   # C
grade3 = get_grade(70)   # B

# Parameters vs arguments

# Parameters: names in the function definition.

def add(a, b):  # a, b are parameters
    return a + b

# Arguments: actual values you pass when calling.

add(3, 5)      # 3, 5 are arguments

# structure of a function

def add(a, b):        #def → tells Python you’re defining a function.
    result = a + b    #add → function name.
    return result     #(a, b) → parameters (inputs).
                      # inside: logic using a and b.
                      # return result → sends the result back.

