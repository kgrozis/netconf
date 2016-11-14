'''
Title    -  2.10. Working with Unicode Chars in Regex 
Problem  -  Using Regex to process text but are concerned about handling Unicode Chars 
Solution -  re module has unicode knowledge
'''

import re

# \d matches any unicode digit char 
num = re.compile('\d+')
# ASCII digits 
print(num.match('123'))
# Arabic digits
print(num.match('\u0661\u0662\u0662'))

# Match all arabic chars in diff arabic code pages
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straBe'
print(pat.match(s)) # Matches
print(pat.match(s.upper())) # Doesn't Match case
print(s.upper()) # Case Folds
