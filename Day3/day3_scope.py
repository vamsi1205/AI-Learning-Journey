x = 10  # global


def modify():
    global x
    x += 5
    print("Inside function:", x)


modify()
print("Outside function:", x)


def get_user_info():
    name = "Vamsi"
    age = 30
    city = "Hyderabad"
    return name, age, city


n, a, c = get_user_info()
print(f"Name: {n}, Age: {a}, City: {c}")
