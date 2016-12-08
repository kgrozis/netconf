'''
Title    -  2.16. Reformatting Text to a Fixed Number of Columns
Problem  -  Have long strings that you want to reformant so that they fill a user specified
              number of columns
Solution -  Use textwrap module to reformat output 
'''

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

# textwrap module straight forward way to clean up text for printing
import textwrap 
print(textwrap.fill(s, 70))
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, subsequent_indent='       '))

# If you want to determine terminal size can use os.get_terminal_size() method 
#   then use textwrap module to keep line wrap under control 

import os
# Doesn't work in IDE
# os.get_terminal_size().columns
