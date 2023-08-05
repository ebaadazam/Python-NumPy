# NUMPY IN PYTHON

# BASICS OF NUMPY

import numpy as np

var2 = np.array([[1, 2, 3, 4, 5], [4, 3, 5, 6, 7], [12, 13, 14, 15, 11]], 'int32')
var = np.array([[1, 2, 3, 4, 5], [4, 3, 5, 6, 7]], 'int16')
temp_var = np.array([10, 20, 30, 40, 50], 'int64')

print('The three dimensional array:', '\n', var2)
print('The two dimensional array:', '\n', var)
print('The one dimensional array:', '\n', temp_var)

# Shape shows row and columns in a tuple
print('row x column', var.shape)
print('row x column', var2.shape)

# Size is nothing but the number of elements in the arrays
print('size of 2D: ', var.size)
print('size of 3D: ', var2.size)

# Gets the array dimension
print('Dimension: ', var2.ndim)
print('Dimension: ', var.ndim)
print('Dimension: ', temp_var.ndim)

# Gets the data type of the array
print(var2.dtype)
print(var.dtype)
print(temp_var.dtype)

# We also have the function just like range in numpy called arrange()
x_values = np.arange(0, 200, 5)
print(x_values)
# [  0   5  10  15  20  25  30  35  40  45  50  55  60  65  70  75  80  85
#   90  95 100 105 110 115 120 125 130 135 140 145 150 155 160 165 170 175
#  180 185 190 195]

# We also have a similar function like arrange() that is linspace().It can contain the last elem as well
# which is not possible in arrange() and it takes the number of items in place of steps
x_values2 = np.linspace(0, 200, 5)
print(x_values2)
# [  0.  50. 100. 150. 200.]


# Accessing/Changing the specific elements, rows, columns etc

num = np.array([[1, 2, 3, 4, 5], [4, 3, 5, 6, 7], [12, 13, 14, 15, 11]])

# [[ 1  2  3  4  5]
#  [ 4  3  5  6  7]
#  [12 13 14 15 11]]

# Accessing the specific row
print(num[0])  # first row will show up
print(num[1])  # second row will show up
print(num[2])  # third row will show up

# Accessing the specific column
print(num[:, 2])  # third column will show up
print(num[:, 4])  # last column will show up
print(num[:, 0])  # first column will show up

# Accessing the specific element
print(num[0, 3])  # 0 represents the first array, 1 represents second and 2 similarly the third one
print(num[1, 2])  # here 1 represents the second array and element at 2 index position


# Getting specific number of elements (StartIndex : EndIndex : StepSize)
print(num[0, -1:-6:-1])  # printing first array in reverse order
print(num[1, 1:4:1])  # [3 5 6]
print(num[2, 2:4:1])  # [14 15]


# Changing the specific elements in the array
num = np.array([[1, 2, 3, 4, 5], [4, 3, 5, 6, 7], [12, 13, 14, 15, 11]])
# [1 2 3 4 5]
# [4 3 5 6 7]
# [12 13 14 15 11]

num[0, 2] = 200  # replace 3 in first array with 200
print(num)
# [[  1   2 200   4   5]
#  [  4   3   5   6   7]
#  [ 12  13  14  15  11]]

num[:, 2] = [1, 2, 3]  # we are changing column no. 3 i.e, [3, 5, 14] to [1, 2, 3]
print(num)
# [[ 1  2  1  4  5]
#  [ 4  3  2  6  7]
#  [12 13  3 15 11]]


# 3D Example
temp3d = np.array([ [[1, 2], [3, 4]], [[5, 6], [7, 8]] ])
print(temp3d)
# [[[1 2]
#   [3 4]]

#  [[5 6]
#   [7 8]]]

# Accessing in 3d array
print(temp3d[0])
# [[[1 2]
#   [3 4]]

print(temp3d[1])
# [[5 6]
#   [7 8]]]

print(temp3d[0, 1])
# [3 4]

print(temp3d[1, 0, 1])  # 6

print(temp3d[:, 0, :])
# [[1 2]
#  [5 6]]

print(temp3d[:, 1, :])
# [[3 4]
#  [7 8]]

# Replace the elements of second rows of both the arrays
temp3d[:, 1, :] = [[11, 11], [22, 22]]
print(temp3d)
# [[[ 1  2]
#  [11 11]]

#  [[ 5  6]
#   [22 22]]]

# Appending the array
append_arr = np.array([1, 2, 3, 4, 5])
append_arr2 = np.append(append_arr, [6, 7, 8, 9])
print(append_arr2)

# Inserting in the array
append_arr = np.array([1, 2, 3, 4, 5])
append_arr2 = np.insert(append_arr, 0, 200)
print(append_arr2)

# Deleting from the array
del_var = np.array([1, 2, 3, 4, 5])
del_var2 = np.delete(del_var, 0)  # delete the item at pos 0
print(del_var2)

# Deleting from the array
del_var = np.array([1, 2, 3, 4, 5, 6, 7, 89, 9])
del_var2 = np.delete(del_var, 5)  # delete the item at pos 5
print(del_var2)

# # Deleting from the array
del_var = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10]])
del_var2 = np.delete(del_var, 0, 0)  # this will delete the whole first row and axis=0
print(del_var2)

# Deleting from the array
del_var = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10]])
del_var2 = np.delete(del_var, 1, 0)  # this will delete the whole second row and axis=0
print(del_var2)

# Deleting from the array
del_var = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10]])
del_var2 = np.delete(del_var, 1, 1)  # this will delete the second column and axis=1
print(del_var2)




# INITIALIZING DIFFERENT TYPES OF ARRAYS

# All 0s matrix
print(np.zeros((3, 3), dtype='float32'))  # this will print 3 x 3 matrix containing 0s and if we put float then
# array values will be in decimal and if we put int then array values will be in integer

# All 1s matrix
print(np.ones((3, 3, 2), dtype='int16'))  # this will print 2 x 3 matrix containing 1s
# In the above the first part i.e, 3 represents how many arrays will be there and the other two represents
# rows and columns

# Any other number
print(np.full((2, 2), 99))  # this will print the matrix of value 99(value can be anything) of the dimensions 2 x 2

# Using full_like
temp3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(np.full_like(temp3d, 5))  # this will convert every element into the number 5 or any other number
# [[[5 5]
#   [5 5]]

#  [[5 5]
#   [5 5]]]

print(np.full_like((2, 2), 5))  # we can also do this using full_like
# [5 5]

# Random decimal numbers
print(np.random.rand(2, 4))  # this will make a 2 x 4 matrix of any random decimal number

# Random Integer values
print(np.random.randint(4, size=(4, 4)))  # this will print a 4x4 matrix with the random numbers less than 4
print(np.random.randint(4, 9, size=(2, 3, 4)))  # this will print a 2x3x4 matrix with the random numbers b/w 4 and 9
print(np.random.randint(-5, 5, size=(3, 4)))  # this will print a 3x4 matrix with the random numbers b/w -5 and 5
print(np.random.choice([10, 20, 30, 40, 50, 60], size=(5, 10)))  # give any random no from the list



# The identity matrix
print(np.identity(4))
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

print(np.identity(2))
# [[1. 0.]
#  [0. 1.]]


# Repeat an array few times
arr = np.array([1, 2, 3])  # make an array
r = np.repeat(arr, 4)  # In the parenthesis of repeat we simply give the arr we want to repeat and no of times
print(r)
# [1 1 1 1 2 2 2 2 3 3 3 3]

arr = np.array([[1, 2, 3]])  # now this has become two dimensional array
r2 = np.repeat(arr, 3, axis=1)  # here axis=1
print(r2)
# [[1 1 1 2 2 2 3 3 3]]

arr = np.array([[1, 2, 3]])  # now this has become two dimensional array
r3 = np.repeat(arr, 3, axis=0)  # here axis=0
print(r3)
# [[1 2 3]
#  [1 2 3]
#  [1 2 3]]

arr = np.array([[1, 2, 3]])  # now this has become two dimensional array
r3 = np.repeat(arr, 5, axis=0)  # here axis=0
print(r3)
# [[1 2 3]
#  [1 2 3]
#  [1 2 3]
#  [1 2 3]
#  [1 2 3]]


# TASK
# Create the matrix below
# [1  1  1  1  1]
# [1  0  0  0  1]
# [1  0  9  0  1]
# [1  0  0  0  1]
# [1  1  1  1  1]

output = np.ones([5, 5], dtype='int32')  # make 5x5 matrix of 1s
sub_output = np.zeros([3, 3], dtype='int32')  # make 3x3 matrix of 0s
sub_output[1, 1] = 9
output[1:4, 1:4] = sub_output  # [1:4, means second(index 1) row to forth(index 3) row & , 1:4] means
# second(index 1) column to forth(index 3) column
print(output)
#[[1 1 1 1 1]
# [1 0 0 0 1]
# [1 0 9 0 1]
# [1 0 0 0 1]
# [1 1 1 1 1]]


# Copying Arrays
a = np.array([1, 2, 4, 6])
b = a  # 'b' is pointing to the same variable that 'a' does, means any change done in 'b' will also be done in 'a'
b[1] = 33
print(b)
# [1 33 4 6]
print(a)
# [1 33 4 6]

c = np.array([2, 4, 6, 8])
d = c.copy()  # but by using copy(), if we make changes in d it will not be happening in c
d[0] = 20
print(d)
# [20  4  6  8]
print(c)
# [2 4 6 8]



# MATHEMATICS
a = np.array([1, 2, 3, 4, 5])
a += 2
print(a)
# [3 4 5 6 7]

a -= 1
print(a)
# [2 3 4 5 6]

a *= 5
print(a)
# [10 15 20 25 30]

b = np.array([10, 10, 10, 10, 10])
print(a+b)
# [20 25 30 35 40]

print(np.sin(a))
# [-0.54402111  0.65028784  0.91294525 -0.13235175 -0.98803162]

print(np.cos(a))
# [-0.83907153 -0.75968791  0.40808206  0.99120281  0.15425145]


# LINEAR ALGEBRA
a = np.ones((2, 3), dtype='int32')
b = np.full((3, 2), 2)
print(np.matmul(a, b))  # multiply both matrices which won't be possible without matmul() as these are of diff sizes

# find the determinant
c = np.identity(3)
print(np.linalg.det(c))

# There are a lot of functions that we perform on numpy arrays like sqrt(), log() etc..

# STATISTICS
st = np.array([[2, 4, 6], [8, 5, 9]])
# [[2 4 6]
#  [8 5 9]]

print(np.min(st))  # returns the minimum element in the entire matrix
print(np.max(st))  # returns the maximum element in the entire matrix
print(np.min(st, axis=1))  # returns the minimum elements of both the arrays row wise i.e, [2 5]
print(np.max(st, axis=1))  # returns the maximum elements of both the arrays row wise i.e, [6 9]
print(np.min(st, axis=0))  # returns the minimum elements of both the arrays col wise i.e, [2 4 6]
print(np.max(st, axis=0))  # returns the maximum elements of both the arrays col wise i.e, [8 5 9]
print(np.sum(st))  # returns sum of both arrays
print(np.sum(st, axis=0))  # returns the sum column wise
print(np.sum(st, axis=1))  # returns the sum row wise


# Reorganizing Arrays
before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(before)
#[[1 2 3 4]
# [5 6 7 8]]

after = before.reshape(4, 2)  # it will convert (2,4) to (4, 2)
print(after)
#[[1 2]
# [3 4]
# [5 6]
# [7 8]]

after = before.reshape(1, 8)  # it will convert (2,4) to (1, 8)
print(after)
# [[1 2 3 4 5 6 7 8]]

# flatten() function
ex = np.array([[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12],
              [13, 14, 15, 16]])
print(ex.flatten())  # this will give us one dimensional view of that
# [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16]

# we can also do this
var = [i for i in ex.flat]  # same output as above but it will print numbers separated by comma inside a list
print(var)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# there is another function that does the same functionality called ravel()


# Swapping the rows and columns
swap = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])
print(swap.transpose())
#[[ 1  5  9 13]
# [ 2  6 10 14]
# [ 3  7 11 15]
# [ 4  8 12 16]]

print(swap.swapaxes(0,1))
# [[ 1  5  9 13]
#  [ 2  6 10 14]
#  [ 3  7 11 15]
#  [ 4  8 12 16]]



# Vertically Stacking Vectors
v1 = np.array([10, 20, 30, 40, 50])
v2 = np.array([1, 2, 3, 4, 5])

print(np.vstack([v1, v1, v2, v2]))
#[[10 20 30 40 50]
# [10 20 30 40 50]
# [ 1  2  3  4  5]
# [ 1  2  3  4  5]]

print(np.vstack([v1, v1, v1, v2]))
#[[10 20 30 40 50]
# [10 20 30 40 50]
# [10 20 30 40 50]
# [ 1  2  3  4  5]]


# Horizontal Stacking Vectors
h1 = np.array([10, 20, 30, 40, 50])
h2 = np.array([15, 25, 35, 45, 55])

print(np.hstack([h2, h1, h2, h1]))
# [15 25 35 45 55 10 20 30 40 50 15 25 35 45 55 10 20 30 40 50]

h3 = np.ones((2, 4))
h4 = np.zeros((2, 2))
print(np.hstack((h3, h4)))
# [[1. 1. 1. 1. 0. 0.]
#  [1. 1. 1. 1. 0. 0.]]



# MISCELLANEOUS

# Load data from file(txt doc)
#file_data = np.genfromtxt('file_name.txt', delimiter=',')  # delimiter means separated by comma
#print(file_data)
#file_data.astype('int32')  # this will convert the data in the file in the integer format



# Boolean Masking and Advanced Indexing

# Here we can check the data in the file
#print(file_data > 50)
# array([[False, False, True]])

#print(file_data[file_data > 50])  # this will give you the values greater than 50
# print(np.any(file_data > 50, axis=1))  # row wise
# print(np.any(file_data > 50, axis=0))  # column wise
# print(np.all(file_data > 50, axis=0))
# print(((file_data > 50) & (file_data < 100)))
# print((~((file_data > 50) & (file_data < 100))))  # ~ means not
# array([23, 44, 55])

# You can index with a list in numpy
a = np.array([1, 2, 4, 6, 8, 10, 12, 14])
print(a[[0, 2, 5]])  # this will return the values present at the index positions 0, 2, and 5.



# Joining and splitting arrays
x = np.array([[1, 2, 3, 4],
               [5, 6, 7, 8]])

y = np.array([[9, 10, 11, 12],
              [13, 14, 15, 16]])

xy = np.concatenate((x, y), axis=0)  # joining arrays row wise
print(xy)

xy = np.concatenate((x, y), axis=1)  # joining arrays column wise
print(xy)

# splitting
new = np.array([[1,  2,  3,  4],
                [5,  6,  7,  8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print(np.split(new, 4, axis=0))
# [array([[1, 2, 3, 4]]), array([[5, 6, 7, 8]]), array([[ 9, 10, 11, 12]]), array([[13, 14, 15, 16]])]

print(np.split(new, 4, axis=1))
# [array([[ 1],
#        [ 5],
#        [ 9],
#        [13]]), array([[ 2],
#        [ 6],
#        [10],
#        [14]]), array([[ 3],
#        [ 7],
#        [11],
#        [15]]), array([[ 4],
#        [ 8],
#        [12],
#        [16]])]

print(np.split(new, 2, axis=1))
# [array([[ 1,  2],
#        [ 5,  6],
#        [ 9, 10],
#        [13, 14]]), array([[ 3,  4],
#        [ 7,  8],
#        [11, 12],
#        [15, 16]])]







