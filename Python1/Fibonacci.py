a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
n_terms = int(input("How many terms of the Fibonacci series to print? "))
print(a, b, end=' ')
for _ in range(n_terms - 2):
    c = a + b
    print(c, end=' ')
    a = b
    b = c
