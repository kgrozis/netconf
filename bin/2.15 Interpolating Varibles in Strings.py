'''
Title    -  2.15. Interpolating Vars in Strings 
Problem  -  Want to create a string in which embedded var names are substituted with a 
              string represetnation of a var's values
Solution -  No support for simply substituting var values in strings.  Can approximate this
              with the format() method 
'''

s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))

# if values to be substituted are found in values, use the combination of format_map() and vars()
# feature of vars is that it works with instances
# Does not handle missing args 
class Info:
  def __init__(self, name, n):
    self.name = name
    self.n = n
a = Info('Guido', 37)
print(s.format_map(vars(a)))

# Define a __missing__ class method to handle missing args 
name = 'Guido'
# del n # make sure n is undefined
class safesub(dict):
  def __missing__(self, key):
    return '{' + key + '}'
print(s.format_map(safesub(vars())))

# Simplify by hiding var sub process behind a small utility function that 
#   employs a 'frame hack'
import sys 
def sub(text):
  return text.format_map(safesub(sys._getframe(1).f_locals))
name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favorite color is {color}'))

# Additional alternative
name = 'Guido'
n = 37
#'%(name) has %(n) messages.' % vars()

#string template 
import string 
s = string.Template('$name has $n messages.')
print(s.substitute(vars()))
