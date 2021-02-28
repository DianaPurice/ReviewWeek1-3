# Ask user for name
print("What is your name human?")
name = str(input())

# Ask user for age
print("\nHow old are you(in years)?")
age = int(input())

# Ask user for height
print("\nHow tall are you (in meters)?")
height = float(input())

# Ask user for weight
print("\nHow much do you weigh (in kg)?")
weight = float(input())

# calculate bmi
bmi = weight / (height ** 2)

print("\n{} you are {} years old and your bmi is {:.2f}.".format(name, age, bmi))