import numpy as np

# concatenate two arrays

arr_1 = np.array([1,2,3])
arr_2 = np.array([4,5,6])
combine = np.concatenate((arr_1, arr_2))
print(combine)

# add new row 

original = np.array([[1,2],[3,4]])
new_row = np.array([[5,6]])
with_new_row = np.vstack((original, new_row))
print(with_new_row)

# add new column

new_column = np.array([[5],[6]])
with_new_column = np.hstack((original,new_column))
print(with_new_column)

# delete any index from row

arr = np.array([1,2,3,4,5,6,7,8,9])
deleted = np.delete(arr, 3)
print(deleted)