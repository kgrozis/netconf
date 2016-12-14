'''
Title    -  Performing Matrix & Linear Algebra Calculations 
Problem  -  matrix multiplication, finding determinants, solving linear
            equations, etc...
'''

# NumPy library, matrix object
import numpy as np 
m = np.matrix([[1,-2,3], [0,4,5], [7,8,-9]])
print(m)
# matrix output is effect with '\n'
# ie - print(m, '\n')
# putting '\n' in it's own staement
print('\n')
# Return transpose 
print(m.T)
print('\n')
# return inverse
print(m.I)

print('\n!---SECTION---\n')

# Create a vector and multiply 
v = np.matrix([[2],[3],[4]])
print(v)
print('\n')
print(m*v)

print('\n!---SECTION---\n')

# numpy.linalg
import numpy.linalg
# Determinant 
print(numpy.linalg.det(m))
# Eigenvalues
print(numpy.linalg.eigvals(m))
# Solve for x in mx = v 
x = numpy.linalg.solve(m,v)
print(x)
print(m*x)