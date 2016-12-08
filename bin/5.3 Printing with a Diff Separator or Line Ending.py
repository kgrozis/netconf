'''
Title    -  5.3 Printing with a diff separator or line ending  
Problem  -  Want to output data using print() but want to change the seperator char 
              or line ending 
Solution -  Use the sep & end keyward args to print()
'''

print('Acme', 50, 91.5)
print('Acme', 50, 91.5, sep=',')
print('Acme', 50, 91.5, sep=',', end='!!\n')

# end can suppress output of newlines 
for i in range(5):
  print(i)
for i in range(5):
  print(i, end=' ')

# str.join() can be similar to sep arg 
# only works with strings
# print(','.join('ACME','50','91.5'))
row = ('ACME', 50, 91.5)
# print(','.join(row))
print(','.join(str(x) for x in row))
# Same code with print sep 
print(*row, sep=',')