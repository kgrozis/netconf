'''
Title    -  2.2. Matching at the Start or End of a String 
Problem  -  Need to check the start or end of a string for specific text patterns 
Solution -  Use str.startswith() method or str.endswitch() method 
'''

filename = 'spam.txt'
print(filename.endswith('.txt')) 
print(filename.startswith('file:'))

url = 'http://www.python.org'
print(url.startswith('http:'))

# Need to check against multiple choices provide a tuple of possibilities 
#   to startswith() or endswith()
import os
filenames = os.listdir('.')
print(filenames)
print('.c or .h:', [name for name in filenames if name.endswith(('.c', '.h'))])
# any() returns a true boleen if condition is meet
print(any(name.endswith('.py') for name in filenames))

from urllib.request import urlopen
def read_data(name):
  if name.startswith(('http:', 'https:', 'ftp:')):
    return urlopen(name).read()
  else:
    with open(name) as f:
      return f.read
print(read_data(url))

# Have a list or set convert to tuple 
choices = ['http:', 'ftp:']
print(url.startswith(tuple(choices)))

# Can use slices for similar behavior as endswith() and startswith
print(filename[-4:] == '.txt')
print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')

# Can use regular expression as an alternative
import re 
print(re.match('http:|https:|ftp:', url))

