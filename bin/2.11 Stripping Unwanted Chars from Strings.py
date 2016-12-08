'''
Title    -  2.10. Working with Unicode Chars in Regex 
Problem  -  Want to strip unwanted chars, from beginning, end or middle of a text string
Solution -  Use strip(), lstrip() or rstrip() methods 
'''

# By default strip() methods strip white space 
# Whitespace stripping 
s = '    hello world  \n'   
print(s.strip())  # strips white space from or end of string
print(s.lstrip()) # strip white space from left side
print(s.rstrip()) # strip white space from right side

#  Character stripping
t = '-----hello======'
print(t.lstrip('-'))
print(t.strip('-='))

# strip() does not apply to the middle of text 
s = '    hello    world   \n'
print(s.strip())  # middle white space remains

# Use replace() for inner space
print(s.replace(' ', ''))
import re
print(re.sub('\s+', ' ', s))  # regex replaces middle space with a single space 

# want to combine stripping operations with an iterative processing 
# use generator expr 
with open(filename) as f:
  lines = (line.strip() for line in f) # transorm data & efficent.  No temp list created 
  for line in lines:
    print('insert operation')


