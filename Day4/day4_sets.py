skills = {"Python", "AWS", "NodeJS", "Python"}  # Duplicates removed
print(skills)

skills.add("AI")
skills.remove("NodeJS")

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
