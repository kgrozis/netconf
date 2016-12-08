'''
Title    -  Performing Complex-Valued Math 
Problem  -  Want to perform math with complex numbers  
Solution -  Complex numbers specified using complex(real, imag) function 
              or by floating-point numbers with a j suffix 
'''

a = complex(2, 4)
b = 3 -5j
print('a:', a)
print('b:', b)

print('\n!---SECTION---\n')

# real, imaginary, & conjugate values 
print('a real:', a.real)
print('a imaginary:', a.imag)
print('a conjugate:', a.conjugate())

print('\n!---SECTION---\n')

# mathematical operators 
print('add:',a+b)
print('multiply',a*b)
print('divide', a/b)
print('absolute value:', abs(a))

print('\n!---SECTION---\n')

# complex-valued functions
import cmath 
print('sine:', cmath.sin(a))
print('consine:', cmath.cos(a))
print('exponenet:', cmath.exp(a))

print('\n!---SECTION---\n')

# math-related modules aware of complex values
# use python 2.7 for numpy
# did not load it into python 3.5
import numpy as np
a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
print('a:', a)
print('a+ 2', a +2)
print('sin(a)', np.sin(a))

# standard math function does not produce complex by default 
# complex math won't show up by accident in code
# error with import math
# will work with import cmath
print('square root -1', cmath.sqrt(-1))