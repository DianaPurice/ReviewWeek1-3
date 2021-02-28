# Ask user for number of lives
print("Please enter the number of lives.")
lives = int(input())

 # Ask user for energy level
print("\nPlease enter the energy level.")
energy = int(input())

# Ask user for shield level
print("\nPlease enter the shield level.")
shield = int(input())
 
# Display results
print("\nHealth has been set.\n")
print("Lives: ", "♥" * lives)
print("Energy: ", "♦" * energy)
print("Shield: ", "♦" * shield)
