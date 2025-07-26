import numpy as np
import matplotlib.pyplot as plt

# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],   # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],   # Beijing Bites
    [3, 200000, 230000, 260000, 300000],   # Pizza Hub
    [4, 180000, 210000, 240000, 270000],   # Burger Point
    [5, 160000, 185000, 205000, 230000],   # Chai Point
])

# print(sales_data.shape)
# print('First three rows restaurants data:\n',sales_data[:3])
# print('All Columns except first of restaurants data:\n',sales_data[:,1:])

# print(np.sum(sales_data, axis=0))   # axis=0 for column
# print(np.sum(sales_data, axis=1))   # axis=1 for row

# yearly_total = np.sum(sales_data[:,1:], axis=0)
# print(yearly_total)

# # minimum sales per restaurant 

# min = np.min(sales_data[:,1:], axis=1)
# print(min)

# # average sales per restaurant

# ave = np.mean(sales_data[:,1:],axis=1)
# print(ave)

# cumulative sales

cumsum = np.cumsum(sales_data[:,1:],axis=1)
print(cumsum)

plt.figure(figsize=(10,5))
plt.plot(np.mean(cumsum, axis=0))
plt.title('Average cumulative sales across all restaurants')
plt.xlabel('Years')
plt.ylabel('Sales')
plt.grid(True)
plt.show()