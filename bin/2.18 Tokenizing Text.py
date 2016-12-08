'''
Title    -  2.18. Tokenizing Text  
Problem  -  Have a string that you wan tto parse left to right into a stream of tokens
Solution -  
'''

text = 'foo = 23 + 42 * 10'

# Need to match & have a way to id pattern
tokens = [('NAME', 'foo'), 
          ('EQ','='),
          ('NUM', '23'), 
          ('PLUS','+'), 
          ('NUM', '42'), 
          ('TIMES', '*'), 
          ('NUM', '10')
          ]

# Define all patterns including whitespace by regex 
import re
# ?P<TOKENNAME> convention assigns name to pattern 
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM  = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ    = r'(?P<EQ>=)'
WS    = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

# scanner method tokenizes 
# creates a scanner object which repeated calls match() and steps thru supplied text 
scanner = master_pat.scanner('foo = 42')
print('Call match():', scanner.match())
_.lastgroup, _.group()