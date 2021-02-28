# Ask user for type of adventure
print("What type of adventure should I have?")
adventure = input()
# Decide the type of adventure
if( (adventure == "scary") or (adventure == "short") ):
    print("\nEnterinng the dark forest!")
elif((adventure == "safe") or (adventure == "long")):
    print("\nTaking the safe route!")

else:
    print("\nNot sure which route to take.")