'''
Title    -  2.13. Aligning Text Strings
Problem  -  Need to format with text with alignment applied
Solution -  Use basic string alignmnet functions: ljust(), rjust(), and center()
'''
text ='Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

# Accepts optional fill chars 
print(text.rjust(20,'='))
print(text.center(20,'*'))

# format() Function using >, <, & ^ and width 
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))

# for filling specify char before alignment char 
print(format(text, '=>20'))
print(format(text, '*^20'))

# Use format codes for multiple values
print'{:>10s} {:>10s}'.format('Hello', 'World')

# Can use format with numbers
x = 1.2345
print(format(x, '>10'))
print(format(x, '^10.2f'))

# older python used % operator to format text 
print('%-20s') % text 
print('%20s') % text 
