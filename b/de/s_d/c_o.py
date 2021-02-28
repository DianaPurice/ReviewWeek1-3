# Ask user for the first numeber
print("Please enter the first number.")
first_number = float(input())

# Ask user for the second number
print("\nPlease enter the second number.")
second_number = float(input())

# decide which number is bigger and display results
if (first_number > second_number):
  print("\nThe second number is the smallest!")
elif (first_number < second_number):
  print("\nThe first number is the smallest!")
else:
  print("Both are equal!")