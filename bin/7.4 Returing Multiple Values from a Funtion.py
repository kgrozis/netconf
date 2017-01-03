'''
Title    -  Returning Multiple Values from a Function   
Problem  -   
'''

# return a tuple of multiple values 
def myfunc():
  return 1, 2, 3
# assigning to multiple values unpacks the tuple
a, b, c = myfunc()
print(a)
print(b)
print(c)

print('\n!---SECTION---\n')

# Comma creates a tuple not parentheses
a = (1,2)
print(a)
b = 1,2
print(b)

print('\n!---SECTION---\n')

# assinig to a single value keeps tuple packed
x = myfunc()
print(x)