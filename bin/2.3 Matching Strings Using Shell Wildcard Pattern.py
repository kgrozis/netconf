'''
Title    -  2.3. Matching Strings Using Shell Wildcard Pattern 
Problem  -  Want to match text using the same wildcard patterns used in Unix shells
Solution -  Use module fnmatch and 2 methods fnmatch() or fnmatchcase()
'''

from fnmatch import fnmatch, fnmatchcase
# fnmatch() uses case-sensitivity rules as the system's underlying OS
print('foo.txt - *.txt:', fnmatch('foo.txt', '*.txt'))
print('foo.txt - ?oo.txt:', fnmatch('foo.txt', '?oo.txt'))
print('Dat45.csv - Dat[0-9]*:', fnmatch('Dat45.csv', 'Dat[0-9]*'))
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print('names:', [name for name in names if fnmatch(name, 'Dat*.csv')])

# fnmatchcase() matches explicitly upper & lower cases
# windows does not check case on file extensions, Mac does
print('foo.txt - *TXT:', fnmatchcase('foo.txt', '*TXT'))

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

print('* ST:', [addr for addr in addresses if fnmatchcase(addr, '* ST')])
print('*CLARK*', [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])
