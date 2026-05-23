import numpy as np

# Create arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print("Array 1:", arr1)
print("Array 2:", arr2)
print()

# Basic operations
print("Addition:", arr1 + arr2)
print("Subtraction:", arr2 - arr1)
print("Multiplication:", arr1 * arr2)
print("Division:", arr2 / arr1)
print()

# Array functions
print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Std Dev:", np.std(arr1))
print("Max:", np.max(arr1))
print("Min:", np.min(arr1))
print()

# 2D Array
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("2D Matrix:")
print(matrix)
print()

# Matrix operations
print("Matrix shape:", matrix.shape)
print("Matrix sum:", np.sum(matrix))
print("Matrix mean:", np.mean(matrix))
print()

# Create special arrays
zeros = np.zeros(5)
ones = np.ones(5)
range_arr = np.arange(0, 10, 2)
linspace_arr = np.linspace(0, 1, 5)

print("Zeros array:", zeros)
print("Ones array:", ones)
print("Range (0 to 10, step 2):", range_arr)
print("Linspace (0 to 1, 5 elements):", linspace_arr)
