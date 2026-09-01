from utils import square, is_even, celsius_to_fahrenheit, greet

# Ask the user for their name
name = input("Enter your name: ")
print(greet(name))

# Ask the user for a number
number = float(input("Enter a number: "))

# Display the square
print("Square:", square(number))

# Check whether the number is even or odd
if is_even(number):
    print("The number is even.")
else:
    print("The number is odd.")

# Convert Celsius to Fahrenheit
print("Fahrenheit equivalent:", celsius_to_fahrenheit(number))