'''
Title    -  Saving Memory When Creating a Large Number of Instances    
Problem  -  Program creates a large number (million) of instances & uses a large amount of memory   
'''

# __slots__ 
# attribute of class definition 
# class that primarily serves as simple data structure 
# reduces memory footprint of instances
# uses compact internal representation
# instance built around a fixed sized array instead of a dict 
# can no longer add new attributes to instances, restricted to names in __slots__ specifier 
class Date:
  __slots__ = ['year', 'month', 'day']
  def __init__(self, year, month, day):
    self.year = year 
    self.month = month 
    self.day = day



print('\n!---SECTION---\n')

