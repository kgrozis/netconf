'''
Title    -  Calculating with Fractions   
Problem  -  Want to do calculations with fractions 
Solution -  Use fractions module 
'''

from fractions import Fraction 
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b)
print(a * b)

# getting numerator/denominator
c = a * b
print(c.numerator)
print(c.denominator)

# converting to a float 
print(float(c))

# Limiting the denominator of a value 
print(c.limit_denominator(8))

# Converting a float to a fraction 
x = 3.75 
y = Fraction(*x.as_integer_ratio())
print(y)

print('\n!---SECTION---\n')
