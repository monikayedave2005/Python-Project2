# Accept a number from the user
num = int(input("Enter a number: "))

# Find the square of the number
square = num * num

# Variable to store the sum of digits
sum_digits = 0

# Store the square value in a temporary variable
temp = square

# Loop to calculate the sum of digits of the square
while temp > 0:
    digit = temp % 10        # Get the last digit
    sum_digits += digit      # Add the digit to the sum
    temp //= 10              # Remove the last digit

# Check whether the sum of digits is equal to the original number
if sum_digits == num:
    print(num, "is a Neon Number.")
else:
    print(num, "is not a Neon Number.")