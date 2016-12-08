'''
Title    -  4.4 Implementing the Iterator Protocol  
Problem  -  Building custom objs and would like ot support iteration 
Solution -  Use generator function 
'''

class Node:
  def __init__(self, value):
    print('__init__')
    self._value = value 
    self._children = []
  def __repr__(self):
    print('__repr__')
    return('Node({!r})'.format(self._value))
  def add_child(self, node):
    print('add_child')
    self._children.append(node)
  def __iter__(self):
    print('__iter__')
    return iter(self._children)
  # Read & Describe 
  def depth_first(self):
    print('depth_first')
    # Yields itself
    yield self
    # Yields children
    for c in self:
      yield from c.depth_first()
# Example
root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
child1.add_child(Node(3))
child1.add_child(Node(4))
child2.add_child(Node(5))
for ch in root.depth_first():
  print(ch)

print('\n', '-'*25, '\n')
# iterator protocl requires __iter__() to return a special iterator object
#   that implemants a next() operation & uses StopIteration exception 
class Node:
  def __init__(self, value):
    print('Node.__init__')
    self._value = value 
    self._children = []
  def __repr__(self):
    print('Node.__repr__')
    return('Node({!r})'.format(self._value))
  def add_child(self, other_node):
    print('Node.add_child')
    self._children.append(other_node)
  def __iter__(self):
    print('Node.__iter__')
    return iter(self._children)
  def depth_first(self):
    print('Node.depth_first')
    return DepthFirstIterator(self)
class DepthFirstIterator(object):
  '''
  Depth-first traversal
  '''
  def __init__(self, start_node):
    print('DepthFirstIterator.__init__')
    self._node = start_node
    self._children_iter = None
    self._child_iter = None
  def __iter__(self):
    print('DepthFirstIterator.__iter__')
    return self 
  def __next__(self):
    print('DepthFirstIterator.__next__')
    # Return myself if just started
    # Create an iterator for children
    if self._children_iter is None:
      self._children_iter = iter(self._node)
      return self._node
    # if processing a child 
    # return its next item 
    elif self._child_iter:
      try: 
        nextchild = next(self._child_iter)
        return nextchild 
      except StopIteration:
        self._child_iter = None 
        return next(self)
    # Advance to teh next child & start its iteration
    else:
      self._child_iter = next(self._children_iter).depth_first()
      return next(self)

root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
child1.add_child(Node(3))
child1.add_child(Node(4))
child2.add_child(Node(5))
for ch in root.depth_first():
  print(ch)