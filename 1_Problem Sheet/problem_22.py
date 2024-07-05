# Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.


def count_dogs_and_chickens(total_heads, total_legs):
    # Each dog has 1 head and 4 legs
    # Each chicken has 1 head and 2 legs
    # Let's assume the number of dogs is x and the number of chickens is y
    # Then, x + y = total_heads (because each dog and chicken has 1 head)
    # And, 4x + 2y = total_legs (because each dog has 4 legs and each chicken has 2 legs)
    # We can solve these two equations to find x and y
    
    # Calculate the number of chickens (y)
    y = (total_legs - 4 * total_heads) // 2
    
    # Calculate the number of dogs (x)
    x = total_heads - y
    
    return x, y

total_heads = int(input("Enter the total number of heads: "))
total_legs = int(input("Enter the total number of legs: "))

dogs, chickens = count_dogs_and_chickens(total_heads, total_legs)

print(f"There are {dogs} dogs and {chickens} chickens.")