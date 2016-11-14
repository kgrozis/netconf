'''
Title    -  2.1. Splitting Strings on Any of Muliple Delimiters 
Problem  -  Need to splita string into fields, but the delimiters aren't 
              consistent throughtout the string 
Solution -  re.split() method offers more flexibility than split() method 
'''

line = 'asdf fjdk; afed, fjek,asdf,      foo'
import re 
# re.split() lets you specify multiple patterns as seperator
# Below comma, semicolon, whitespace or extra whitespace used to seperate
# Whenever the pattern is found, entire match becomes the delimiter 
#   between whatever fields lie on either side of the match  
print(re.split(r'[;,\s]\s*', line))

# if capture group is in parenthesis are used then matched text is also 
#   included
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

#  Gettting split characters are useful if you need to reform string
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)

# Reform the line using the same delimiters
print(''.join(v+d for v,d in zip(values, delimiters)))

# Results without seperates, but using parentheses
# Use a noncapture group, (?:...)
print(re.split(r'(?:,|;|\s)\s*', line))
