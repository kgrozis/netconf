'''
Title    -  1.2 Unpacking Elements from Iterables of Arbitrary Length
Problem  -  Need to unpack N element from an iterable, but the iterable may be longer
              than N elements, causing a 'too many values to unpack' exception
Solution - Use the operator module's itemgetter function.
'''

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print('fname:\n',rows_by_fname)
print('uid:\n',rows_by_uid)

# itemgetter() can accept multiple keys 
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print('lfame:\n', rows_by_fname)