'''
Title    -  Calculating with Large Numerical Arrays 
Problem  -  Perform calcs on large numerical datasets 
Solution -  Use Numpy library for heavy computation involving arrays 
'''

# numpy gives python an rray obj that is more efficent for math calcs 
#  than standard python lists 
# Python Lists
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(x*2)
# Cannot use + operator with an integer
# x + 10
# add operator with a list 
print(x + y)

print('\n!---SECTION---\n')

# Numpy arrays
# +, * operations with another list happen on an index basis
# +, * operations with a numeric apply to all indexes
import numpy as np 
ax = np.array([1,2,3,4])
ay = np.array([5,6,7,8])
print(ax * 2)
print(ax + 10)
print(ax + ay)
print(ax * ay)

print('\n!---SECTION---\n')

def f(x):
  return 3*x**2 - 2*x + 7
print(f(ax))

print('\n!---SECTION---\n')

# numpy universal functions for array operations
# much faster than looping thru values 
print(np.sqrt(ax))
print(np.cos(ax))

print('\n!---SECTION---\n')

# can make large scale arrays
# arrays made in same manner as c or fortrain
grid = np.zeros(shape=(10000,10000), dtype=float)
print(grid)
# array operations still apply
grid += 10
print(grid)
print(np.sin(grid))

print('\n!---SECTION---\n')

# extends python's list indexing functionality
# multi-dimensional arrays
a = np.array([1,2,3,4], [5,6,7,8], [9,10,11,12])
print(a)
# select row 1
print(a[1])
# select column 1
print(a[:,1])