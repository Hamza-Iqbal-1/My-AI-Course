import numpy as np

# simple filteration 
 
numbers = np.array([1,2,3,4,5,6,7,8,9,10])
# filter even numbers from this array
even_numbers = numbers[numbers % 2 ==0]
print(even_numbers)

# Filtration with mask

mask = numbers > 5      # evaluates expression and gives numbers greater than 5
print('numbers greater than 5: ', numbers[mask])

indices = [0,2,4]       # evaluate expression and gives indies of array
print('indices of array: ', numbers[indices])

# Filtration with np.where()

where_result = np.where(numbers>5)
print(numbers[where_result])
