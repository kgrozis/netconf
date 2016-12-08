'''
Title    -  3.2 Performing Accurate Decimal Calculations   
Problem  -  Need to perform accurate calcs with decimal numbers
              don't want the small errors that naturally occur with floats
              floats don't accurately represent all base-10 decimals
Solution -  Use the csv library 
'''

# Errors are part of underlying CPU & IEEE 754 arthmetic peformed by float unit 
# Python stores float data as native representations.
# Nothing to do to avoid errors 
a = 4.2
b = 2.1
print(a+b)
print((a+b)==6.3)

# More accuracy with decimal module 
# Sacrifices performance
from decimal import Decimal
# Specify numbers as strings 
# If print or format they behave like numbers  
a = Decimal('4.2')
b = Decimal('2.1')
print(a+b)
print((a+b)==6.3)

# Control number of digits and rounding 
from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a/b)
with localcontext() as ctx:
  ctx.prec = 3
  print(a/b)
with localcontext() as ctx:
  ctx.prec = 50
  print(a/b)

# subtractive cancellations and adding large & smal numbers together 
nums = [1.23e+18, 1, -1.23e+18]
print('Sum:',sum(nums)) # 1 disappears

import math 
print(math.fsum(nums))

