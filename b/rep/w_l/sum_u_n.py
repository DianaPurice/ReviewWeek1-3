#ask for numbers
print("How many numbers should I sum?")
n_to_sum = int(input())

# declare a control variable

summed = 1

# sum numbers
total = 0

while (summed <= n_to_sum):
  print("Please enter number ",summed , "of", n_to_sum)
  number = float(input())
  total = total + number
  summed = summed + 1
#display results
print("The answer is", total)