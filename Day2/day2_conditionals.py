age = int(input("Enter your age: "))

if age >= 18 and age < 25:
    print("You’re a young adult.")
elif age < 5:
    print("You're a toddler.")
elif age < 13:
    print("You're a child.")
elif age < 20:
    print("You're a teenager.")
elif age < 60:
    print("You're an adult.")
else:
    print("You're a senior.")
