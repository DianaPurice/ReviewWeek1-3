# Ask user for sound
print("What did I hear?")
sound = input()

# Ask user for view
print("\nWhat did I see?")
view = input()

# Determinate what action to take
if ((sound == "grrr") and (view == "two red eyes")):
  print("\nThere is a scary creature. I should get out of here!")
else:
  print("\nI am a little scared but i will continue.")