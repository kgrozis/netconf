'''
Title    -  2.5. Searching and Replacing Text 
Problem  -  Want to search for & replace a text pattern in a string 
Solution -  For simple literal patterns use str.replace() method
'''

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

# For more complicated patterns use the sub functions / methods in re module 
# First arg is pattern to match. 
# Second arg is replacement pattern.
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

# Compile pattern for repeated substition.  Get better performance
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))

# Substition Callback function
from calendar import month_abbr
def change_date(m):
  mon_name = month_abbr[int(m.group(1))]
  return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
print(datepat.sub(change_date, text))

# Want to know how many subs were made in addition to getting the replacement text use re.subn 
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext)
print(n)
