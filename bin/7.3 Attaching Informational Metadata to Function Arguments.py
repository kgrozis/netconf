'''
Title    -  Attaching Informational Metadata to Function Arguments  
Problem  -  Want to attach some additionl info to the args 
            others will know more about how function is supposed to be used 
'''

# Function Arg Annotations 
# Give programmers hints about how a function is supposed to be used 
# int syntax is hints, not type checks
# interpreter ignores hints

def add(x:int, y:int) -> int:
  return x + y

# appear in function documentation
help(add)

print('\n!---SECTION---\n')

# __annotations__
# Stores function annotations 
# Primary use documentation
print(add.__annotations__)

print('\n!---SECTION---\n')

