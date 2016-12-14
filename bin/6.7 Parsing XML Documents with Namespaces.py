'''
Title    -  Parsing XML Docs with Namespaces   
Problem  -  Parse an XML Doc that's using XML namespaces 
Solution -  Use xml.etree.ElementTree
'''

# Read & make changes to pred.xml 
from xml.etree.ElementTree import parse, Element
doc = parse('namespace.xml')
root = doc.getroot()
print(root)

# working queries
print(root.findtext('author'))
print(root.find('content'))

# query involving a namespace doesn't work 
print(doc.find('content/html'))

# works if fully qualified 
print(doc.find('content/{http://www.w3.org/1999/xhtml}html'))

# doesn't work
print(doc.findtext('content/{http://www.w3.org/1999/xhtml}html/head/title'))

# Fully Qualified
print(doc.findtext('content/{http://www.w3.org/1999/xhtml}html/'
  '{http://www.w3.org/1999/xhtml}head/{http://www.w3.org/1999/xhtml}title'))

print('\n!---SECTION---\n')

# wrap name space handling into a utility class 
class XMLNamespaces:
  def __init__(self, **kwargs):
    print('@__init__()')
    self.namespaces = {}
    for name, uri in kwargs.items():
      self.register(name, uri)
  def register(self, name, uri):
    print('@register')
    self.namespaces[name] = '{'+uri+'}'
  def __call__(self, path):
    print('@__call__')
    return path.format_map(self.namespaces)

ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
print(root.find(ns('content/{html}html')))
print('\n!---SECTION---\n')
print(root.findtext(ns('content/{html}html/{html}head/{html}title')))

print('\n!---SECTION---\n')

# No mechanism in ElementTree to get further info about namespaces
# get more info about the scope of namespace processing by using iterparse()
from xml.etree.ElementTree import iterparse 
for evt, elem in iterparse('namespace.xml', ('end', 'start-ns', 'end-ns')):
  print(evt, elem)
print(elem)

# examine lxml library