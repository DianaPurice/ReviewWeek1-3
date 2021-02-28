# ask user for the cover type
print("What type of cover does the book have (hard or soft)?")
cover_type = input()

# Decide if cover is soft of hard
if (cover_type == "soft"):
  # Decide if the bound is perfect or not
  print("\nIs the book perfect bound?")
  perfect_bound = input()
  if (perfect_bound == "yes"):
    print("\nSoft cover, perfect bound books are very popular!")
  else:
    print("\nSoft covers with coils or stitches are great for short books")

else:
  print("\nBooks with hard covers can be more expensive!")