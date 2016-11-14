'''
Title    -  2.8.Writing a regex for multiline patterns  
Problem  -  Trying ot match a block of text using a regex, but need to span multiple lines
              dot (.) matches all chars except newline 
Solution -  use a noncapture group 
'''

import re

# Trying ot match C-Style comments
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a 
              multiline comment */
'''
print(comment.findall(text1))
# matches nothing
print(comment.findall(text2))

# add support for newlines
# (?:.|\n) specifies a noncapture group - defines a group for the purpose of matching
#   but that group is not captured separately or numbered
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))

# re.compile accepts a flag re.DOTALL which makes . a regex that matches all chars 
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))
