'''
Title    -  2.7. Specifying a Regular Expression for the Shortest Match  
Problem  -  Use regex to find the shortest possible match   
Solution -  use re module and supply re.IGNORECASE flag to operations
'''

import re

# Problem occurs in patterns that try to match text enclosed inside a quoted string.
# Try to match expr in quotes 
# * operator matchs on longest possible match 
# . char matches any chars except newline
# if you bracket . with "" it will attempt to find longest match 
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text2 = 'Computer syas "no."  Phone says "yes."'
# incorrectly matches the two quoted strings
print(str_pat.findall(text2))

# adding ? operator to * or + makes expr a shortest match 
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))