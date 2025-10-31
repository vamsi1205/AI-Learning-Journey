students = {}

while True:
    print("\n--- Student Grade Tracker ---")
    print("1. Add student")
    print("2. View all students")
    print("3. Update marks")
    print("4. Delete student")
    print("5. Average marks")
    print("6. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ").strip().lower()
        marks = float(input("Enter marks: "))
        students[name] = marks

    elif choice == "2":
        if students:
            print("\n--- Student List ---")
            for name, marks in students.items():
                print(f"{name}: {marks}")
        else:
            print("\n⚠️ No students yet! Add someone first.")

    elif choice == "3":
        name = input("Enter name to update: ").strip().lower()
        if name in students:
            students[name] = float(input("Enter new marks: "))
        else:
            print("Student not found!")

    elif choice == "4":
        name = input("Enter name to delete: ")
        students.pop(name, None)

    elif choice == "5":
        if students:
            avg = sum(students.values()) / len(students)
            print("Average marks:", round(avg, 2))
        else:
            print("No students yet!")

    elif choice == "6":
        break

    else:
        print("Invalid choice!")
