import numpy as np

customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])

active_indices = np.where(last_purchase_days_ago <= 30)[0]
active_customers = customer_ids[active_indices]

inactive_indices = np.where(last_purchase_days_ago > 30)[0]
inactive_customers = customer_ids[inactive_indices]

print("Active Customers (Last Purchase <= 30 days ago):")
print(active_customers)

print("\nInactive Customers (Last Purchase > 30 days ago):")
print(inactive_customers)
