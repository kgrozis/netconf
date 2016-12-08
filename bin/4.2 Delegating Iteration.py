'''
Title    -  4.2 Delegating Iteration   
Problem  -  Build a custom container & want to make iteration work
Solution -  define __iter__() method that delegates itertion to the interally held container 
'''

class Node:
  def __init__(self, value):
    print('Node.__init__()')
    self._value = value 
    self._children = []
  def __repr__(self):
    print('Node.__repr__()')
    return 'Node({!r})'.format(self._value)
  def add_child(self, node):
    print('Node.add_child()')
    self._children.append(node)
  # implements a __next__() method to carryout iteration 
  def __iter__(self):
    print('Node.__iter__()')
    # forwards iter() request to internal held _children attribute
    return iter(self._children)

root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
for ch in root:
  print(ch) # outputs Node(1), Node(2)

