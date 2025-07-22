import numpy as np

# for one dimensional array

unsorted = np.array([3,1,2,1,6,8,4,9,5,7])
print("Sorted array", np.sort(unsorted))   # convert unsorted array into sorted array

# for two dimensional array

arr_2d = np.array([[1,3,2],
                   [2,1,3],
                   [3,2,1]])
print('sorted 2d array by column', np.sort(arr_2d, axis=0))    # by column
print('sorted 2d array form by row', np.sort(arr_2d, axis=1))  # by row

