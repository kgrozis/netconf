'''
Title    -  Parsing, Modifying, & Rewriting XML   
Problem  -  Read an XML doc, make changes to it, and write it as XML 
Solution -  Use xml.etree.ElementTree
'''

# Read & make changes to pred.xml 
from xml.etree.ElementTree import parse, Element
doc = parse('pred.xml')
root = doc.getroot()
print(root)
# remove elements 
root.remove(root.find('sri'))
root.remove(root.find('cr'))
# insert new elements after <nm> ... </nm>
print(root.getchildren().index(root.find('nm')))
e = Element('spam')
e.text = 'This is a test'
root.insert(2, e)
# write back to file 
doc.write('newpred.xml', xml_declaration=True)

print('\n!---SECTION---\n')

# use io.BytesIO for binary data
from io import BytesIO
s = BytesIO()
s.write(b'binary data')
print(s.getvalue())
