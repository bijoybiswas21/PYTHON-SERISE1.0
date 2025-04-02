import pandas as pd

# Creating Series1
Series1 = pd.Series([100, 200, 300, 400, 500], index=['A', 'B', 'C', 'D', 'E'])

# Doubling the values in Series1 and storing them in Series2
Series2 = Series1 * 2

print("Series1:")
print(Series1)
print("\nSeries2:")
print(Series2)
