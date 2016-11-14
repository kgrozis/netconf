'''
Title    -  1.5 Implementing a Priority Queue
Problem  -  Want to implement a queue that sorts items by a given priority and
              always returns the item with the highest priority on each pop operation
Solution -  Use heapq
'''

import heapq

class PriorityQueue:
  def __init__(self):
    print('PriorityQueue.__init__()')
    # list used by heapq
    self._queue = []
    self._index = 0
  def push(self, item, priority):
    print('PriorityQueue.push()')
    # heappush inserts items into a list
    # tuple is added to list with this structure 
    # priority is negated to search from highest to lowest priority
    # _index var orders items with a priority level
    # _index also does comparison of same priority and reduces priority for same item
    heapq.heappush(self._queue, (-priority, self._index, item))
    self._index += 1
  def pop(self):
    print('PriorityQueue.pop()')
    # heappop removes items from a list 
    # always returns the lowest value in list
    return heapq.heappop(self._queue)[-1]

class Item:
  def __init__(self, name):
    print('Item.__init__()')
    self.name = name
  def __repr__(self):
    print('Item.__repr()__')
    return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
# Pop returns the highest priority item 
# If an item has the same priority, then the first entered is returned
print('Pop:', q.pop())
print('Pop:', q.pop())
print('Pop:', q.pop())
print('Pop:', q.pop())

a = Item('foo')
b = Item('bar')
# The Item object can't be ordered without priority queue
# Thus comparisons can't be done.  
# The following comparison creates an exception
# a < b

a = (1, Item('foo'))
b = (5, Item('bar'))
# if you make a tuple you can compare Item object
print('Compare:', a < b)
# You cannot compare the same value
c = (1, Item('grok'))
# Creates an exception
# a < c

# adding a 3rd value of index to the tuple.  You can now compare.
# Python won't compare remaining tuple values once it has a result 
a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))
print('Compare:', a < b)
print('Compare:', a < c)

