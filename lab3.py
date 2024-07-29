import numpy as np

category1_revenue = np.array([500, 600, 700, 550])
category2_revenue = np.array([450, 700, 800, 600])

total_revenue = category1_revenue + category2_revenue

print("Total Revenue:", total_revenue)



print("*****************************************")
revenue = np.array([10000, 12000, 11000, 10500])
expenses = np.array([4000, 5000, 4500, 4800])

profit = revenue - expenses

print("Profit:", profit)

print("*************************************")
inventory = np.array([10, 0, 5, 0, 20, 0])

out_of_stock_products = np.where(inventory == 0)[0]

print("Out of Stock Products:", out_of_stock_products)
print("*************************************")

# calculate the total cost of items in a shopping cart, considering the quality and price per item 
quantity = np.array([2,3,4,1])
price_per_item= np.array([10.0,5.0,8.0,12.0])
 

cost_per_item = quantity * price_per_item

total_cost = np.sum(cost_per_item)

print("Cost per item: ", cost_per_item)
print("Total cost: $", round(total_cost, 2))