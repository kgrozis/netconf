'''
Title    -  6.3 Parsing Simple XML Data  
Problem  -  Want to extract data from a simple XML doc 
Solution -  use xml.etree.ElementTree Module 
'''

from urllib.request import urlopen 
# parses entire XML doc into a doc obj 
from xml.etree.ElementTree import parse 
# Download the RSS feed and parse it
u = urlopen('http://planet.python.org/rss20.xml')
doc= parse(u)
# Extract & ouptut tags of interest
# doc.iterfind finds top-level in tree 
for item in doc.iterfind('channel/item'):
  # findtext finds attribute in branch
  title = item.findtext('title')
  date = item.findtext('pubDate')
  link = item.findtext('link')
  print(title)
  print(date)
  print(link)
  print()

print(doc)
e = doc.find('channel/title')
print(e)
print(e.tag)
print(e.text)
print(e.get('some attribute'))

# also research lxml module
# similar methods but faster