'''
Title    -  5.1 Reading and Writing Text Data  
Problem  -  Need to read or write text data 
Solution -  Use the open() function with mode rt to read a text file  
'''

# Read the entire file as a single string
with open('somefile.txt', 'rt') as f:
  data = f.read()
  print(data)
print('-'*10)
# Iterate over the lines of the file 
with open('somefile.txt', 'rt') as f:
  for line in f:
    print(line)

text1 = 'Text one of file'
text2 = '\nText two of file'
# to write a text file use open() with mode 'wt' to write a file 
#   clearing & overwriting the previous contents (if any)
# Write chunks of text data
with open('somefile.txt', 'wt') as f:
  f.write(text1)
  f.write(text2)
line1 = '\nLine one of file'
line2 = '\nLine two of file'
# Redirected print statement
# to append to an existing fiel use open() mode at 
with open('somefile.txt', 'at') as f:
  print(line1, file=f)
  print(line2, file=f)

# by default, files are read/write using the system default text coding 
#   sys.getdefaultencoding() returns type of encoding
#   most macines use utf-8
# Supply optional encoding paramter if you know type 
with open('somefile.txt', 'at', encoding='latin-1') as f:
  print(line1, file=f)
  print(line2, file=f)

# with 'with' statement control is kept in block of code 
#   file is automatically closed on exit of block 
# without 'with' statement file remains open 
f = open('somefile.txt', 'rt')
data = f.read()
print(data)
f.close()

# newline - unix is \n and window is \r\n 
# python uses universal newline and recognizes all newline chars 
#   newline chars are converted to '\n'
# don't want newline conversion
with open('somefile.txt', 'rt', newline='') as f:
  for line in f:
    print(line)

# encoding / decoding errors 
#  f = open('sample.txt', 'rt', encoding='ascii')
# UnicodeDecodeError is exception for bad decode 
#   Not decoding in right encode 
# f.read()
# replace bad chars with Unicode U+fffd replacement char 
# f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
#   f.read()
# ignore bad chars entirely 
# g = open('sample.txt', 'rt', encoding='ascii', errors='ignore')
#   g.read() 