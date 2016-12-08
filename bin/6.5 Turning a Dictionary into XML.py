'''
Title    -  6.5 Turning a Dictionary into XML 
Problem  -  Want to take the data in a Python Dict & turn it into XML 
Solution -  Use xml.etree.ElementTree library
'''

from xml.etree.ElementTree import Element
def dict_to_xml(tag, d):
  '''
  Turn a simple dict of key/value pairs into xml
  '''
  elem = Element(tag)
  for key, val in d.items():
    child = Element(key)
    child.text = str(val)
    elem.append(child)
  return elem 
s = { 'name': 'GOOG', 'shares': 100, 'price':490.1 }
e = dict_to_xml('stock', s)
print(e)

print('\n!---SECTION---\n')

# for i/o convert byte string using tostring() function
from xml.etree.ElementTree import tostring 
print(tostring(e))
# attach elements to elements by using set() method
e.set('_id', '1234')
print(tostring(e))
# if order matters use an OrderedDict

print('\n!---SECTION---\n')

# when creating XML, might be inclined to make strings 
def dict_to_xml_str(tag, d):
  '''
  Turn a simple dict of key/value pairs into XML 
  '''
  parts = ['<{}>'.format(tag)]
  for key, val in d.items():
    parts.append('<{0}>{1}</{0}>'.format(key, val))
  parts.append('</{}>'.format(tag))
  return ''.join(parts)
# problem occurs when dict values contain special chars 
d = {'name':'<spam>'}
# String creation
print(dict_to_xml_str('item', d))
# Proper XML creation
# replaces < and > with &lt; and &gt;
e = dict_to_xml('item', d)
print(tostring(e))

print('\n!---SECTION---\n')

# if you need to escape or unescape chars
# use escape() or unescape() from xml.sax.saxutils
from xml.sax.saxutils import escape, unescape 
print(escape('<spam>'))
print(unescape('_'))