n = int(input("Enter the size of the array: "))
arr = []
for _ in range(n):
    element = int(input("Enter an element: "))
    arr.append(element)

print(f"The sum of array elements is: {sum(arr)}")
