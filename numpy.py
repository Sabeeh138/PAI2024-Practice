import numpy as np

# simple aray
a = np.array([1, 2, 3])
print(a)

# 2D Array
b = np.array([[2.0, 3.0, 4.0], [6.0, 7.0, 8.0]])
print(b)

# How to get dimensions of an array
print(b.ndim) # dimensions of array b

# How to get shape of an array
print(b.shape) # array b is a 2x3 array

# How to get the datatype of an array
print(a.dtype) 
print(b.dtype)

# We can set the datatype/size of an array by ourselves
sized_array = np.array([1, 2, 3], dtype='int16')
print(sized_array.dtype)

# How to get the size of an element of an array
print(a.itemsize)
print(b.itemsize)
print(sized_array.itemsize)

# How to get the size of the whole array
print(a.nbytes)
print(b.nbytes)
print(sized_array.nbytes)


import numpy as np

# # All 0s matrix
# zero_matrix = np.zeros((2, 3, 2, 3), dtype='int32')
# print(zero_matrix)

# Array of random decimal numbers
# random_matrix = np.random.rand(2, 3)
# print(random_matrix)

# Array of random int numbers
# random_int_matrix = np.random.randint(7, size=(2, 3))
# print(random_int_matrix)

# initializing an identity matrix
# identity_matrix = np.identity(4)
# print(identity_matrix)

# If we want to initialize an array by repeating another array
# repeat_array = np.repeat([[[1, 2, 3]]], 3, axis=1)
# print(repeat_array)

# question:
# array to be made:
#   [[1, 1, 1, 1, 1]
#    [1, 0, 0, 0, 1]
#    [1, 0, 9, 0, 1]
#    [1, 0, 0, 0, 1]
#    [1, 1, 1, 1, 1]]
# array = np.ones((5, 5))
# temp_array = np.zeros((3, 3))
# temp_array[1, 1] = 9
# array[1:4, 1:4] = temp_array
# print(array)


import numpy as np

# BOOLEAN MASKING AND ADVANCED INDEXING

filedata = np.genfromtxt('Numpy_Array.txt', delimiter=',')

# print(filedata > 50) # returns Booleans for wherever the condition is true or false

# print(filedata[filedata > 50]) # return the values in the array which meet the condition

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# print(array[[2, 3, 8]]) # returns the elements at index 2, 3, and 8

# print(np.any(filedata > 50, axis=0)) # this checks for a value greater than 50 in each column
# print(np.any(filedata > 50, axis=1)) # this checks for a value greater than 50 in each row

# print(np.all(filedata > 50, axis=0)) # this checks if all values are greater than 50 in each column
# print(np.all(filedata > 50, axis=1)) # this checks if all values are greater than 50 in each row




import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]]) # a 2x7 array

# How to get a specific element, indexing: [row, column]
#print(a[1, 5])

# How to get a complete row
#print(a[0, :]) 

# How to get a complete column
#print(a[:, 2])

# Another approach to extract elements from the array, [start_index : end_index : step_size]
#print(a[0, 0 : 7 : 1]) # this prints the first row starting with index 0, step_size 1, end_index 7

# How to change a specific element
# a[1, 5] = 100 # 100 replaces 13
# print(a)

# How to change the values of a specific row with a same value
# a[1, :] = 50
# print(a)

# How to change the values of a specific column with a same value
# a[:, 3] = 35
# print(a)

# How to change values of a specific row with different values
# a[0, :] = [7, 6, 5, 4, 3, 2, 1]
# print(a)

# How to change values of a specific column with different values
# a[:, 5] = [69, 70]
# print(a)

# 3D array example
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(b)
# if we need to access '4' in this array:
#print(b[0, 1, 1])
# if we need to change some value in the 3D array
# b[1, 1, 1] = 69 # here 8 will change to 69
# b[0, :, :] = [[3, 3], [3, 3]]
# print(b)


import numpy as np

# array = np.array([[1, 2, 3], [4, 5, 6]])

# add 2 to each element, subtraction multiplication and division is done in the same way
# array += 2
# print(array)

# array2 = np.array([[3, 2, 1], [6, 5, 4]])
# print(array2 + array)

# Raising an array to some power
# print(array ** 2)

# we can get values of trigonometric functions of arrays
# print(np.cos(array))

# LINEAR ALGEBRA WITH NUMPY
# a = np.ones((2, 3))
# b = np.full((3, 2), 2)

# print(np.matmul(a, b)) # for this calculation the columns of the first matrix must be equal to the rows of the second matrix

# determining the determininat of a matrix
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(np.linalg.det(matrix))

# STATISTICS WITH NUMPY
array = np.array([[1, 2, 3], [4, 5, 6]])
# print(np.max(array)) # max of the whole array
# print(np.min(array)) # min of the whole array
# print(np.max(array, axis=1)) # max of each row
# print(np.median(array)) # median of the array
# print(np.sum(array)) # the sum of all the elements in the array
# print(np.sum(array, axis=1)) # sum of each row
# print(np.sum(array, axis=0)) # sum of each column

# REORGANIZING ARRAYS
initial_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print("Initially the array is in the form: \n", initial_array)
new_array = initial_array.reshape(4, 2)
# print("The New Array Is In The Form: \n", new_array)

# VERTICALLY STACKING VECTORS
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
# print(np.vstack((v1, v2))) # vertically stacking vectors
# OR
# print(np.vstack([v1, v2, v1, v2]))

# HORIZONTALLY STACKING VECTORS
# print(np.hstack((v1, v2))) # horizontally stacking vectors
