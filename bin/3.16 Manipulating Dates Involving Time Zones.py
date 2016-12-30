'''
Title    -  Manipulating Dates Involving Time Zones  
Problem  -  
'''

# pytz module 
# olson time zone database 
# de facto std for time zone info 
# datetime module 
# localizing dates with datetime library 
from datetime import datetime 
from pytz import timezone 
d = datetime(2012, 12, 21, 9, 30, 0)
print('STD:',d)
# localize date for chicago 
central = timezone('US/Central')
loc_d = central.localize(d)
print('Chicago:',loc_d)

print('\n!---SECTION---\n')

# once date is localize it can be converted to other time zones 
# convert to Bangalore time 
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print('Bangalore:',bang_d)

print('\n!---SECTION---\n')

# normalize()
# Date arithmetic 
# Daylight savings time
from datetime import timedelta
d = datetime(2013,3,10,1,45)
loc_d = central.localize(d)
print('Chicago:',loc_d)
later = loc_d + timedelta(minutes=30)
print('+30min', later)
later = central.normalize(loc_d + timedelta(minutes=30))
print('+30min Normalized', later)

print('\n!---SECTION---\n')

# convert all dates to UTC time 
# use that for all internal storage & manipulation
print(loc_d)
utc_d = loc_d.astimezone(timezone('UTC'))
print(utc_d)
# no dayligth saving time in UTC
later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central))

print('\n!---SECTION---\n')

# validate timezone by country code
from pytz import country_timezones
print(country_timezones['IN'])