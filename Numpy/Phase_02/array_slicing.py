import numpy as np

arr = np.arange(10)
print(arr)

# slicing in one dimensional arrays

print('basic slicing',arr[2:7])
print('slicing with steps', arr[1:8:2])
print('negative indexing', arr[-1])

# slicing in two dimensional arrays by giving specific row and column

arr_2d = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print('specific element', arr_2d[2,1])
print('Entire row: ', arr_2d[2])       # print 3nd row
print('Entire column', arr_2d[:, 2])   # print 3rd column