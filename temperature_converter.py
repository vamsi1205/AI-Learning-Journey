temp = float(input("Enter temperature: "))
unit = input("Is it in (C/F)? ").upper()

if unit == "C":
    converted = (temp * 9/5) + 32
    print(f"Converted: {converted:.2f}°F")
elif unit == "F":
    converted = (temp - 32) * 5/9
    print(f"Converted: {converted:.2f}°C")
else:
    print("Invalid unit!")
