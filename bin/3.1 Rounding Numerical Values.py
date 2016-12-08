'''
Title    -  2.18. Tokenizing Text  
Problem  -  Want to round a floating-point number to a fixed number of decimal places
Solution -  Use built-in round(value, ndigits) function 
'''

# When a value is halfway between 2 choices 
# rounds to the neareest even digit 
# 1.5 & 2.5 round to 2
print(round(1.23, 1))
print(round(1.27, 1))
print(round(-1.27, 1))
print(round(1.25361, 3))

# round() is not the same as format()
x = 1.23456
print(format(x, '0.2f'))
print(format(x, '0.3f'))
print('value is {:0.3f}'.format(x))

# don't use round() to fix precision errors
# use decimal() module 
a = 2.1
b = 4.2
c = a + b
print('c:', c)
print(round(c, 2))
