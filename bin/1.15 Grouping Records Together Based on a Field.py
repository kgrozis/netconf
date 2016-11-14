'''
Title    -  1.15 Grouping Records Together Based on a Field
Problem  -  Have a seq of dictionaries or instances and want to iterate over 
              the data in groups based on the value of a particular field
Solution -  Use itertools.groupby() function 
'''

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# want to iterate over data in chunks grouped by date 
# sort by date and then use itertools.groupby()
from operator import itemgetter
# groupby() method scans a seq & finds sequential 'runs' of identical values 
#   It returns the value along with an iterator (all items in a group with same value)
#   Important to sort data first to group records
from itertools import groupby

# Sort by the desired field first
rows.sort(key=itemgetter('date'))

# iterate in groups 
for date, items in groupby(rows, key=itemgetter('date')):
  print(date)
  for i in items:
    print('     ', i)

# Want to group data together by data into a large data struct with random access 
#   better to use defaultdict() and build a multidict
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
  rows_by_date[row['date']].append(row)
for r in rows_by_date['07/01/2012']:
  print(r)