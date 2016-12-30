'''
Title    -  Converting Strings into Datetimes  
Problem  -  App receives temporal data in string format 
            Want to convert strings into datetime objs 
            in order to perform nonstring ops on them   
'''

# datetime.strptime()
# supports formatting codes 
# can support formatting codes in reverse  
from datetime import datetime 
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y 
print('Datetime:', diff)

print('\n!---SECTION---\n')

# strptime()
# worse performance, written in Python
# better pefromance to write on module 
def parse_ymd(s):
  year_s, mon_s, day_s = s.split('-')
  return datetime(int(year_s), int(mon_s), int(day_s))

print('\n!---SECTION---\n')
