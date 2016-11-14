'''
Title    -  1.3 Keeping the Last N Items
Problem  -  Want to keep a limited history of the last few items seen during 
              iteration or during some other kind of processing
Solution -  Use collections.deque
'''

from collections import deque

def search(lines, pattern, history=5):
  # creates a fixed size queue with a default of 5 length
  # when queue is full oldest item is automatically removed
  previous_lines = deque(maxlen=history)
  for line in lines:
    if pattern in line:
      yield line, previous_lines
    previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
  with open('somefile.txt') as f:
    for line, prevlines in search(f, 'python', 5):
      for pline in prevlines:
        print(pline, end='')
      print(line, end='')
      print('-'*20)

# queues are more elegant than list and run faster
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print('3 items q:', q)
q.append(4)
print('4 items q:', q)
q.append(5)
print('5 items q:', q)

# creates simple queue structure 
# if you give a max size your queue is unbounded
# an unbounded queue can be appened and popped on either end
q = deque()
q.append(1)
q.append(2)
q.append(3)
print('3 items q:', q)
q.appendleft(4)
print('4 items q:', q)
print('pop q:', q.pop())
print('5 items q:', q)
print('pop q left:', q.popleft())
