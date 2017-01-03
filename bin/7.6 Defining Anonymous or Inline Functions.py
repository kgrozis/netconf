'''
Title    -  Defining Anonymous or Inline Functions   
Problem  -  Need to supply a short callback function for use with an operation 
            Don't want to write a seperate one-line function using def statement
            Want shortcut that allows you to specify the function 'in line'  
'''

# lambda expr 
# simple funcs that do nothing more than evaluate an expr
# expr after : 
# return before : 
add = lambda x,y: x+y 
print(add(2,3))
print(add('hello ', 'world'))

print('\n!---SECTION---\n')

# lambda
# can be used in the context of other operations
# such as sorting or data reduction 
names = ['David Beazley', 'Brian Jones',
         'Raymond Hettinger', 'Ned Batchelder']
print(sorted(names, key=lambda name: name.split()[-1].lower()))

print('\n!---SECTION---\n')





