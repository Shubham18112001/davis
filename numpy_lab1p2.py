import numpy as np

monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])

quarter_1 = monthly_sales[0:3]
quarter_2 = monthly_sales[3:6]
quarter_3 = monthly_sales[6:9]
quarter_4 = monthly_sales[9:12]

print("Quarter 1 Sales (in thousands of dollars):")
print(quarter_1)

print("\nQuarter 2 Sales (in thousands of dollars):")
print(quarter_2)

print("\nQuarter 3 Sales (in thousands of dollars):")
print(quarter_3)

print("\nQuarter 4 Sales (in thousands of dollars):")
print(quarter_4)
