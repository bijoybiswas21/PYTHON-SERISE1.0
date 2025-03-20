""" # 1. For loop with range
for i in range(1, 6):
    print(f"Counting: {i}")

# 2. While loop with counter
count = 0
while count < 5:
    print(f"Current count: {count}")
    count += 1

# 3. Nested loops for multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("-" * 10)

# 4. Loop with break and continue
for num in range(10):
    if num == 3:
        continue  # Skip 3
    if num == 8:
        break    # Stop at 8
    print(num)"""

# 5. Loop through a list with enumerate
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")