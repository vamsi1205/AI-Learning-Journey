# Define a function
def greet(name):
    print(f"Hello {name}, welcome to your AI journey!")


# Call it
greet("Vamsi")


# Function with return value
def add(a, b):
    return a + b


print("Sum:", add(5, 3))


# Default arguments
def power(base, exp=2):
    return base**exp


print(power(3))
print(power(2, 5))
