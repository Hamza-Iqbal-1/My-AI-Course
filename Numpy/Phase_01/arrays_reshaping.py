import numpy as np

arr = np.arange(12)
print(arr)     # it prints flat array

# reshaped this array into 3 rows and 4 columns
reshape = arr.reshape((3,4))
print(reshape)

# reshaped (3,4) array into flat array
flat = reshape.flatten()
print(flat)

# ravel method returns original instead of copy
# it is same like flat but flat returns copy and it returns original
raveled = flat.ravel()
print(raveled)

# transpose matrix 
# transpose means convert rows into columns and columns into rows
transpose = reshape.T
print(transpose)