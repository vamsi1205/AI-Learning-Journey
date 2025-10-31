# Creating and accessing
fruits = ["apple", "banana", "mango"]
print(fruits[0])  # apple

# Modifying
fruits.append("orange")
fruits.insert(1, "grapes")
print(fruits)

# Removing
fruits.remove("banana")
print(fruits)
last = fruits.pop()
print("Removed:", last)

# Slicing
# Starting Index : Ending Index (excludes ending index, includes starting index element)
print(fruits[0:2])

# Looping
for fruit in fruits:
    print(fruit.upper())
