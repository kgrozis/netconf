'''
Title    -  Changing the String Representation of Instances 
Problem  -  Change the output produced by printing or viewing
            instances to something more sensible 
'''

# __str__()
# converts instance to a string 
# ouptut produced by the str() & print() functions
# __repr__()
# returns the code representation of an instance 
# text you would type to re-create the instance 
class Pair:
  def __init__(self, x, y):
    print('__init__')
    self.x = x
    self.y = y
  def __repr__(self):
    print('__repr__')
    # !r is formatting code for __repr__
    # common to create a useful textual representation of 
    # instance using '<state>' format
    return '< Pair({0.x!r}, {0.y!r}) >'.format(self)
  def __str__(self):
    # !s is formatting ocde for __str__
    print('__str__')
    return '({0.x!s}, {0.y!s})'.format(self)
p = Pair(3,4)
p        # __repr__() output
print(p) # __str__() output

print('\n!---SECTION---\n')

p = Pair(3,4)
# calls __repr__
print('p is {0!r}'.format(p))
# calls __str__
print('p is {0}'.format(p))

print('\n!---SECTION---\n')

f = open('file.dat')
# eval(repr(f))