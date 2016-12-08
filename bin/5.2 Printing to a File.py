'''
Title    -  5.2 Printing to a file   
Problem  -  Want to redirect the output of the print() function to a file 
Solution -  Use file keyword arg to print()
'''

with open('somefile.txt', 'rt') as f:
  print('Hello World!', file=f)