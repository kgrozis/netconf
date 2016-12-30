'''
Title    -  Writing Functions that only Accept Keyword Arguments  
Problem  -  Want a function to only accept certain args by keyword
'''

# * arg 
# place keyword args after * arg 
def recv(maxsize, *, block):
  'receives a msg'
  pass 

# print(recv(1024, True))
# TypeError

print(recv(1024, block=True))  # OK

print('\n!---SECTION---\n')

# varying number of positional args 
def mininum(*values, clip=None):
  m = min(values)
  if clip is not None:
    m = clip if clip > m else m
  return m
print(mininum(1,5,2,-5,10))          # varying positional args with no keyword
print(mininum(1,5,2,-5,10,clip=0))   # varying positional args with keyword

print('\n!---SECTION---\n')

# keyword-only args enforce greater code clarity
msg = recv(1024, block=False)
print(msg)

print('\n!---SECTION---\n')

# help()
# args show up when help function is invocked 
# *arg & **kwargs will not give user help() on var context
help(recv)