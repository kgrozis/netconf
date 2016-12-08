'''
Title    -  2.17. Handling HTML and XML Entities in Text 
Problem  -  Want to replace HTML or XML entities with corresponding text or need to
              prouce text, but escape certain chars 
Solution -  Use html.escape() function 
'''

s = 'Elements are written as "<tag>text</tag>".'

import html

print(s)
print(html.escape(s))

# Disabling escaping of quotes 
print(html.escape(s, quote=False))

# Trying to emit code as ASCII and want to embed char code entities for non-ASCII chars
s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))

# Use html.parser() method to automatically replace values and do parsing 
s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
print(p.unescape(s))

t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))
