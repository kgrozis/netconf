'''
Title    -  6.1. Reading & Writing CSV Data  
Problem  -  Want to read or write data encoded as a CSV file 
Solution -  Use the csv library 
'''

import csv 
# row will be tuple 
# access fields using tuple[index] 
with open('stocks.csv') as f:
  f_csv = csv.reader(f)
  headers = next(f_csv)
  for row in f_csv:
    print(row)

# Use named tuples 
# can use row.<header> to access value instead index 
from collections import namedtuple
with open('stocks.csv') as f:
  f_csv = csv.reader(f)
  headings = next(f_csv)
  Row = namedtuple('Row', headings)
  for r in f_csv:
    row = Row(*r)
    print(row)

# read data as a seq of dictionaries 
# access attribute using the row['<header']
with open('stocks.csv') as f:
  f_csv = csv.DictReader(f)
  for row in f_csv:
    print(row)

# create a writer object 
headers = ['Symbol','Price','Date','Time','Change','Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
        ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
        ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
       ]
# with open('stocks.csv', 'w') as f:
#  f_csv = csv.writer(f)
#  f_csv.writerow(headers)
#  f_csv.writerows(row)

# change the seperator char to tab 
with open('stocks.tsv') as f:
  f_tsv = csv.reader(f, delimiter='\t')
  for row in f_tsv:
    print(row)

# creating header row is tougher in now-csv files 
# header will fail with a ValueError exception 
# scrub header with a regex expression 
import re 
with open('stocks.csv') as f:
  f_csv = csv.reader(f)
  headers = [ re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv) ]
  Row = namedtuple('Row', headers)
  for r in f_csv:
    row = Row(*r)
    print(row)

# csv does not interpret data or convert to a type 
# all fields are a string 
# need to manually convert 
col_types = [ str, float, str, str, float, int ]
with open('stocks.csv') as f: 
  f_csv = csv.reader(f)
  headers = next(f_csv)
  for row in f_csv:
    # apply conversions to the row items 
    row = tuple(convert(value) for convert, value in zip(col_types, row))
    print(row)

# alternatively covert select values of a dict 
print('Reading as dict with type conversions')
field_types = [ ('Price', float),
                ('Change', float),
                ('Volume', int) ]
with open('stocks.csv') as f:
  for row in csv.DictReader(f):
    row.update((key, conversion(row[key]))
               for key, conversion in field_types)
    print(row)