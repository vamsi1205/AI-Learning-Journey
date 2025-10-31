with open("notes.txt", "w") as file:
    file.write("AI is the future.\n")
    file.write("Python makes it possible.\n")
    file.write("Learning daily with discipline.\n")

with open("quotes.txt", "w") as file:
    print("------------------------ Enter Three Quotes One by One -----------------")
    for i in range(3):
        quote = input(f"Enter Quote {i+1}: ")
        file.write(f"{quote}\n")

with open("quotes.txt", "r") as file:
    print("\nYour Saved Quotes:")
    for line in file:
        print("-", line.strip())
