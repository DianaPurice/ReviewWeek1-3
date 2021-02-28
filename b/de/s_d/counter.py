# Ask user for first number
print("Please enter the first whole number.")
first = int(input())

# Ask user for second whole number
print("\nPlease enter the second whole number.")
second = int(input())

# Ask user for third whole number
print("\nPlease enter the third whole number.")
third = int(input())

# Define variable even and odd
even = 0
odd = 0
# Determinate if first number is even or odd
if (first % 2 == 0):
  even = even + 1
else:
  odd = odd +1

# Determinate if second number is even or odd
if (second % 2 == 0):
  even = even + 1
else:
  odd +=1

# Determinate if third number is even or odd
if (third % 2 == 0):
  even = even +1
else:
  odd +=1

# Display result
print("\nThe are {} even and {} odd numbers.".format(even, odd))
