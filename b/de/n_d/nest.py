# ask user where to look
print("Where should I look?")
answer = input()

# bedroom
if (answer == "in the bedroom"):
  # Decide if the bound is perfect or not
  print("\nWhere in the bedroom should I look?")
  bedroom = input()
  if (bedroom == "under the bed"):
    print("\nFound some shoes but no battery.")
  else:
    print("\nFound some mess but no battery.")

elif (answer == "in the bathroom"):
  print("\nWhere in the bathroom should I look?")
  bathroom = input()
  if (bathroom == "in the bathtub"):
    print("\nFound a rubber duck but no battery.")
  else:
    print("\nFound a wet surface but no battery.")
elif (answer == "in the lab"):
  print("\nWhere in the lab should I look?")
  lab = input()
  if (lab == "on the table"):
    print("\nYes! I found my battery!")
  else:
    print("\nFound some tools but no battery!")
else:
  print("\nI do not know where that is but I will keep looking.")