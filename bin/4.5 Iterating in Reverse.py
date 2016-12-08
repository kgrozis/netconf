'''
Title    -  4.5 Iterating in Reverse 
Problem  -  Want to iterate in reverse over a seq 
Solution -  Use built-in reversed() function 
'''

a = [1,2,3,4]
# reversed will only work if size can be determined
for x in reversed(a):
  print(x)

# if no size can be determined
# must convert obj to list 
# print file backwards 
# beware converting into a list could consume alot of memory 
f = open('somefile.txt')
for line in reversed(list(f)):
  print(line, end='')

# customize reversed iteration on a user defined class with __reversed__() method 
class Countdown:
  def __init__(self, start):
    self.start = start 
  #Forward Iterator 
  def __iter__(self):
    n = self.start 
    while n > 0:
      yield n
      n -= 1
  # Reverse Iterator 
  def __reversed__(self):
    n = 1
    while n <= self.start:
      yield n
      n += 1
c = Countdown(5)
for x in c:
  print(x)
for x in reversed(c):
  print(x)