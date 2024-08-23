############################################################################
# Take input from the user
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print("The number", number, "is even.")
else:
    print("The number", number, "is odd.")

############################################################################
# Generate the multiplication table
print("Multiplication Table of", number)
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

############################################################################
# Take input from the user
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Find the largest number
largest_number = max(number1, number2, number3)

# Print the result
print("The largest number is", largest_number)


############################################################################
# Take input from the user
string = input("Enter a string: ")

# Initialize a counter for vowels
vowel_count = 0

# Iterate through each character in the string
for char in string:
    # Check if the character is a vowel
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += 1

# Print the result
print("The number of vowels in", string, "is", vowel_count)
