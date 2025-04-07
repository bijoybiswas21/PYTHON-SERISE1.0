import pandas as pd

# Initialize empty lists for each column
names = []
ids = []
salaries = []

# Loop to collect user inputs
for i in range(5):
    name = input(f"Enter Employee {i+1} Name: ")
    emp_id = input(f"Enter Employee {i+1} ID: ")
    basic_salary = float(input(f"Enter Employee {i+1} Basic Salary: "))
    
    # Append inputs to respective lists
    names.append(name)
    ids.append(emp_id)
    salaries.append(basic_salary)

# Create a DataFrame from the lists
df = pd.DataFrame({
    "Employee Name": names,
    "Employee ID": ids,
    "Basic Salary": salaries
})

# Display the DataFrame
print(df)
