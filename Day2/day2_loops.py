for i in range(5):
    print("Iteration:", i)

count = 0
while count < 5:
    print("Count is:", count)
    count += 1

for i in range(1, 10):
    if i == 5:
        continue  # Skip 5
    if i == 8:
        break  # Stop loop
    print(i)
