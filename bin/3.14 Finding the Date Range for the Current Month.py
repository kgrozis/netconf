'''
Title    -  Finding the Date Range for the Current Month   
Problem  -  code nees to loop over each date in the current month 
            want an efficent way to calc date range 
'''

# datetime.timedelta 
# loop over the date 
from datetime import datetime, date, timedelta 
import calendar 
def get_month_range(start_date=None):
  if start_date is None:
    start_date = date.today().replace(day=1)
  _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
  end_date = start_date + timedelta(days=days_in_month)
  return (start_date, end_date)

print('\n!---SECTION---\n')

a_day = timedelta(days=1)
print(a_day)
first_day, last_day = get_month_range()
print(first_day, last_day)

print('\n!---SECTION---\n')

while first_day < last_day:
  print(first_day)
  first_day += a_day

print('\n!---SECTION---\n')

# Use generator to increment thru month 
def date_range(start, stop, step):
  while start < stop:
    yield start
    start += step 

for d in date_range(datetime(2012, 9, 1), datetime(2012,10,1), timedelta(hours=6)):
  print(d)
  
print('\n!---SECTION---\n')



print('\n!---SECTION---\n')

