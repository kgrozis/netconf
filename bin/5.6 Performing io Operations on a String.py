'''
Title    -  Performing io Operations on a String  
Problem  -  Feed a text or binary string to code that's been written to oerate
              on file-like objects instead 
Solution -  Use io.string() or io.byte classes to create file objects that operate 
              on string data
'''

from io import StringIO
s = StringIO()
print(s.write('Hello World\n'))
print('This is a test', file=s)
# gets all data writen
print(s.getvalue())
# wrap a file interface an existing string 
s = StringIO('Hello\nWorld\n')
print(s.read(4))
print(s.read())

print('\n!---SECTION---\n')

# use io.BytesIO for binary data
from io import BytesIO
s = BytesIO()
s.write(b'binary data')
print(s.getvalue())