# ask user how many bars should be charged
print("How many bars should be charged?")
bars = int(input())
print()

# create variable
charged = 0

# while loop
while (charged < bars):
  charged +=1
  print("Charging:", "# " * charged)
 

print("\nThe battery is fully charged.")