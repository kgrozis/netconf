'''
Title    -  5.5 Writing to a File That Doesn't already Exist
Problem  -  Want to write data to a file, but it doesn't exist in filesystem
Solution -  Solve with x mode in open instead of w mode 
'''

with open('somefile', 'wt') as f:
  f.write('Hello\n')
# will error if file already exists 
# raises FileExistError exception 
#with open('newfile2', 'xt') as f:
#  f.write('Hello\n')
# if file is binary use 'xb' mode 

# test for a file 
import os
if not os.path.exists('somefile'):
  with open('somefile', 'wt') as f:
    f.write('Hello\n')
else:
  print('File Already Exists!')