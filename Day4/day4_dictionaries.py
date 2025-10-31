person = {"name": "Vamsi", "age": 30, "city": "Hyderabad"}

print(person["name"])
person["profession"] = "Engineer"
print(person)

# Looping
for key, value in person.items():
    print(f"{key}: {value}")

# Safe access
print(person.get("hobby", "Not specified"))
