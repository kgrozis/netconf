'''
Title    -  Customizing String Formatting   
Problem  -  Object supporting customized formatting through format() 
'''

# __format__() 
_formats = { 
  'ymd' : '{d.year}-{d.month}-{d.day}',
  'mdy' : '{d.month}/{d.day}/{d.year}',
  'dmy' : '{d.day}/{d.month}/{d.year}'
}
class Date:
  def __init__(self, year, month,day):
    self.year = year
    self.month = month
    self.day = day
    print(type(self).__name__ + '.__init__')
  def __format__(self, code):
    print(type(self).__name__ + '.__format__()')
    if code == '':
      code = 'ymd'
    fmt = _formats[code]
    return fmt.format(d=self)
d = Date(2012, 12, 21)
print(format(d))
print(format(d, 'mdy'))
print('The date is {:ymd}'.format(d))
print('The date is {:mdy}'.format(d))

print('\n!---SECTION---\n')

from datetime import date
d = date(2012, 12, 21)
print(format(d))
from datetime import date 
print(format(d, '%A, %B, %d, %Y'))