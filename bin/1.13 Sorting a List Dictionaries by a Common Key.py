'''
Title    -  1.13 Sroting a List of Dictionaries by a Common Key 
Problem  -  Have a list of dictionaries and you would like to sort the entries
              according to one or more of the dictionary values
Solution -  Use operator.itemgetter() method
'''

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# output rows ordered by any of the fields
# itemgetter can be used on dictionary key, numeric list element or
#   anything that from object __getitem__() method
#   returns a tuple than can be sorted by a method like sorted()
from operator import itemgetter

# rows are passed to built-in sorted() function which accepts a key arguement
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print('fname:\n', rows_by_fname)
print('uid:', rows_by_uid)

# itemgetter accepts multiple Keys
rows_by_lfame = sorted(rows, key=itemgetter('lname', 'fname'))
print('multiple keys:\n', rows_by_lfame)

# using lambda for an inline function 
# does the same as itemgetter() but runs slower
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lname = sorted(rows, key=lambda r: (r['lname'],r['fname']))
print('fname:\n', rows_by_fname)
print('multiple keys:\n', rows_by_lfame)

# can apply to min() or max() functions
print('MIN:', min(rows, key=itemgetter('uid')))
print('MAX:', max(rows, key=itemgetter('uid')))

