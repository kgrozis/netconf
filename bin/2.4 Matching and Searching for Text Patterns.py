'''
Title    -  2.4. Matching & Searching for Text Patterns 
Problem  -  Want to match or search text for a specific patterns
Solution -  If match is a simple literal can use basic string methods 
'''

text = 'yeah, but no, but yeah, but no, but yeah'
# Exact match
print('Exact Match:', text == 'yeah')
# Match at start or end 
print('Starts with:', text.startswith('yeah'))
print('Ends with:', text.endswith('no'))
# Search for the location of the first occurence
print('Find:', text.find('no'))

# Use regular expressions and the re module for complicated matching
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
# Simple matching: \d+ means match one or more digits 
if re.match(r'\d+/\d+/\d+', text1):
  print('yes')
else:
  print('no')
if re.match(r'\d+/\d+/\d+', text2):
  print('yes')
else:
  print('no')

# For lots of matching on the same pattern precomplie regular expression into a pattern obj 
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
  print('yes')
else:
  print('no')
if datepat.match(text2):
  print('yes')
else:
  print('no')

# findall() method finds all occurance of text 
text = 'Today is 11/27/2012.  PyCon starts 3/12/2013.'
print(datepat.findall(text))

# Create capture group by enclosing parts of the pattern in parentheses
# The contents of each group can be extracted individually
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print('m:', m)
# Extract the contents of each group 
print('m0', m.group(0))
print('m1', m.group(1))
print('m2', m.group(2))
print('m3', m.group(3))
print('m', m.groups())
month, day, year = m.groups()

# Find all matches (notice splitting into tuples)
# Finds all text matches and returns them as list 
print(text)
print('findall:', datepat.findall(text))
for month, day, year in datepat.findall(text):
  print('{}-{}-{}'.format(year, month, day))

# find matches iteratively 
# returns as tuples
for m in datepat.finditer(text):
  print(m.groups())

# match() only checks the beginning of a string
m = datepat.match('11/27/2012abcdef')
print(m)
print(m.group())
# use end-maker ($) for an exact match 
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
print(datepat.match('11/27/2012abcdef'))
print(datepat.match('11/27/2012'))
# Skip compilation & use module level functiono in re module()
print(re.findall(r'(\d+)/(\d+)/(\d+)', text))