# Ask user for painting direction 
print("Towards which direction should I paint (up, down, left or right)?")
direction = input()

# declare statement if..elif..else
if (direction == "up"):
  print("\nI am painting in the upward direction!")
elif (direction == "down"):
  print("\nI am painting in the downward direction!")
elif (direction == "left"):
  print("\nI am painting in the leftward direction!")
elif (direction == "right"):
  print("\nI am painting in the rightward direction!")
else:
  print("\nI do not understand this direction!")