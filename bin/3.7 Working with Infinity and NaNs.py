'''
Title    -  Working with Infinity and NaNs  
Problem  -  Need to create or test for the floating point values of inifinity, 
              negative infinity, or Not a Number  
Solution -  Create using float()
'''

a = float('inf')
b = float('-inf')
c = float('nan')
print('a', a)
print('b', b)
print('c', c)

print('\n!---SECTION---\n')

import math

# test for the presence of the values
print(math.isinf(a))
print(math.isnan(c))

print('\n!---SECTION---\n')

# infiinite values will propagate in clacs in a math manner
print(a + 45)
print(a * 10)
print(10 / a)

print('\n!---SECTION---\n')

# Some operations are undefined & will result in a NaN result 
print(a/a)
print(a + b)

print('\n!---SECTION---\n')

# NaN values propagate without raising an exception 
print(c+23)
print(c/2)
print(c*2)
print(math.sqrt(c))

print('\n!---SECTION---\n')

# NaN numbers never compare as equal 
d = float('nan')
print(c==d)
print(c is d)
