'''
Title    -  6.4. Parsing Huge XML Files Incrementally 
Problem  -  Need to extract data from a huge XML doc using as little 
              memory as possible 
Solution -  Use iterators & generators for incremental data processing
'''

# process huge XML files using a very small memory foot print
from xml.etree.ElementTree import iterparse
def parse_and_remove(filename, path):
  path_parts =  path.split('/')
  doc = iterparse(filename, ('start', 'end'))
  # skip the root element 
  next(doc)
  tag_stack = []
  elem_stack = []
  for event, elem in doc:
    if event == 'start':
      tag_stack.append(elem.tag)
      elem_stack.append(elem)
    elif event == 'end':
      if tag_stack == path_parts:
        yield elm
        elem_stack[-2].remove(elm)
      try:
        tag_stack.pop()
        elem_stack.pop()
      except IndexError:
        pass

from xml.etree.ElementTree import parse
from collections import Counter
potholes_by_zip = Counter() 
doc = parse('potholes.xml')
for pothole in doc.iterfind('row/row'):
  potholes_by_zip[pothole.findtext('zip')] += 1
for zipcode, num in potholes_by_zip.most_common():
  print(zipcode, num)

print('\n', '-'*25, '\n')

