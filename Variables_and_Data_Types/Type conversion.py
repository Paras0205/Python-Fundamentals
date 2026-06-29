#Python often needs you to convert text input into numbers using int(), float(), or str().

# Example: Converting a string to an integer

# Convert a string number into integer and add 10.
num_str = input("Enter a number: ")
num_int = int(num_str)
result = num_int + 10
print("The result is:", result)

#Convert temperature input into float and calculate Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

#Take age as input and calculate year of birth.
age = int(input("Enter your age: "))
current_year = 2026
year_of_birth = current_year - age
print("You were born in the year:", year_of_birth)
