n = int(input("Enter a number n: "))
sum_odd = 0
for i in range(1, n + 1, 2):
    sum_odd += i
print("Sum of odd numbers from 1 to", n, "is:", sum_odd)
