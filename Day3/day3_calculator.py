def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b if b != 0 else "Division by zero!"


while True:
    print("\n--- Calculator ---")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /, ** or q to quit): ")

    if op == "q":
        print("Goodbye!")
        break
    elif op == "+":
        print("Result:", add(a, b))
    elif op == "-":
        print("Result:", sub(a, b))
    elif op == "*":
        print("Result:", mul(a, b))
    elif op == "/":
        print("Result:", div(a, b))
    elif op == "**":
        print("Result:", a**b)
    else:
        print("Invalid operation!")
