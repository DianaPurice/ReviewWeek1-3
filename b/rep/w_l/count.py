# Ask user for how many cables to be removed
print("How many cables must I avoid?")
avoid = int(input())

# Create variable to track number of live cables
live = 0

# Using a while loop
print()

while (live < avoid):
  print("Avoiding...", end="") 
  live = live+1
  print("Done! {} live cables avoided.".format(live))

# display final message
print()
print("All live cables have been avoided.")