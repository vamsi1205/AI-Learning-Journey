coordinates = (10.5, 20.3)
print(coordinates[0])

# Trying to modify (will cause error)
# coordinates[0] = 11.0  ❌

# Tuple unpacking
x, y = coordinates
print(f"x: {x}, y: {y}")

# Looping
for coordinate in coordinates:
    print(coordinate)
