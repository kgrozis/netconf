'''
Title    -  3.3 Need to format a number for output 
Problem  -  Want to read or write data encoded as JSON 
Solution -  Use built-in format() function 
'''

x = 1234.56789
# 2 decimal places of accuracy
print(format(x,'0.2f'))
# Right justified in 10 chars, 1 digit accuracy
print(format(x, '>10.1f'))
# left justified 
print(format(x, '<10.1f'))
# centered
print(format(x, '^10.1f'))
# inclusion of thousands separator 
print(format(x, ','))
print(format(x, '0,.1f'))

# exponatial notation uses e vs f 
print(format(x, 'e'))
print(format(x, '0.2E'))

# .format() method of strings
print('The value is {:0,.2f}'.format(x))

# techniques work with Decimal numbers in decimal modules 
# values are rounded with same rules of round() function 
print(x)
print(format(x, '0.1f'))
print(format(-x, '0.1f'))

# thousand seperator (,) is not locale aware
# Can swap chars using the translate()
swap_separators = { ord('.'):',', ord(','):'.' }
print(format(x, ',').translate(swap_separators))

# Using % operator instead of format 
print('%0.2f' % x)
print('%10.1f' % x)
print('%-10.1f' % x)