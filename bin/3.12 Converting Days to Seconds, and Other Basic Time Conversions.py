'''
Title    -  Converting Days to Seconds, & Other Basic Time Conversions  
Problem  -  Perform simple time conversions
'''

# datetime module
# Perform conversions & arthmetic involving different units of time   
# datetime.timedelta()
# represent an interval of time 
from datetime import timedelta 
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b 
print(c.days)
print(c.seconds)
print(c.seconds/3600)
print(c.total_seconds()/3600)

print('\n!---SECTION---\n')

# dateime()
# represent specific dates & times 
# use standard math operations to manipulate 
from datetime import datetime
a = datetime(2012, 9, 23)
print(a + timedelta(days=10))
b = datetime(2012, 12, 21)
d = b - a 
print(d.days)
now = datetime.today()
print(now)
print(now + timedelta(minutes=10))

print('\n!---SECTION---\n')

# datetime()
# aware of leap years 
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
print(a-b)
print((a-b).days)
c = datetime(2013, 3, 1)
d = datetime(2012, 2, 28)
print((c-d).days)

print('\n!---SECTION---\n')

# dateutil module 
# complex date manipulations - time zones, fuzzy time ranges, calc dates of holidays 
# dateutil.relativedelta()
# handles dates with differing number of days 
a = datetime(2012, 9,23)
# month invalid as an arg 
# a + timedelta(months=1)
from dateutil import relativedelta
print(a + relativedelta(months=+1))

print('\n!---SECTION---\n')

