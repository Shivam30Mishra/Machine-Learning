# Numpy is a general purpose array-processing package. It provides a high-performance multidimensional array object, and tools for working with these arrays. It is the fundamental package for scientific computing with Python.

# Numpy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

import numpy as np

# Creating a numpy array
a = np.array([1, 2, 3])
print(a)

# converting list to array using numpy
b = [4, 5, 6]
c = np.array(b)
print(c)
print(type(c))

# making two dimensional array from list
lst1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
d = np.array(lst1)
print(d)


# use of np.shape
print(d.shape)

# retrieving first and last column of multidimensional array
print(d[:, [0, -1]])

# numpy array from indexing point of view
print("numpy array from indexing point of view")
# print(d>2)
# print(d[d>2])

# reshaping the array to 3x3
print("rehaping the array to 3x3")
e = np.arange(9).reshape(3, 3)
print(e)
print(e*e)

# np.ones() method use
print("np.ones() method use")
f = np.ones((3, 3))
print(f)

# np.random.randit() method use
print("np.random.randit() method use")
g = np.random.randint(1, 10, (3, 3))
print(g)
h = np.random.randint(1, 10, 3)
print(h)

# np.random.randn() method use
print("np.random.randn() method use")
# return a sample from standard normal distribution means mean = 0 and variance = 1 stnadard deviation = 1
i = np.random.randn(3, 3)
print(i)

# np.random.random_sample() method use
print("np.random.random_sample() method use")
j = np.random.random_sample((3, 3))
print(j)