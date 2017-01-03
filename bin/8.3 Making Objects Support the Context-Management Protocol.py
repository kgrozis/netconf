'''
Title    -  Making Objects Support the Context-Management Protocol  
Problem  -  Make objects support the context-mgmt protocol (with statement)
'''

# __enter__()
# __exit__()
# Creates a network connection 
# __init__ does not start connection 
# with statement establishes & closed connection 
from socket import socket, AF_INET, SOCK_STREAM
class LazyConnection:
  def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
    self.address = address 
    self.family = AF_INET
    self.type = SOCK_STREAM
    self.sock = None
    print('__init__({}, {})'.format(address, family))
  def __enter__(self):
    print(type(self).__name__ + '.__enter__()')
    # allows single connection 
    if self.sock is not None:
      raise RuntimeError('Already Connected')
    self.sock = socket(self.family, self.type)
    self.sock.connect(self.address)
    return self.sock 
  def __exit__(self, exc_ty, exc_val, tb):
    print(type(self).__name__ + '.__exit__()')
    self.sock.close()
    self.sock = None
from functools import partial 
conn = LazyConnection(('ww.python.org', 80))
# Connection is closed 
with conn as s:
  # conn.__enter__() executes: connection opens
  # return value placed in as (var: s) 
  s.send(b'GET / index.html HTTP/1.0\r\n')
  s.send(b'Host: www.python.org\r\n')
  s.send(b'\r\n')
  resp = b''.join(iter(partial(s.recv, 8192), b''))
  # conn.__exit__() executes: connection closed 
  # if return value True exceptions cleared 

print('\n!---SECTION---\n')

class LazyConnection:
  def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
    self.address = address 
    self.family = AF_INET
    self.type = SOCK_STREAM
    # keeps connection stack 
    self.connections = []
    print('__init__({}, {})'.format(address, family))
  def __enter__(self):
    print(type(self).__name__ + '.__enter__()')
    sock = socket(self.family, self.type)
    sock.connect(self.address)
    # add to connection stack
    self.connections.append(sock)
    return sock 
  def __exit__(self, exc_ty, exc_val, tb):
    print(type(self).__name__ + '.__exit__()')
    # pops connection list & exits connection 
    self.connections.pop().close()
from functools import partial 
conn = LazyConnection(('ww.python.org', 80)) 
# multiple connections with a nested with statement
with conn as s1:
  s1.send(b'GET / index.html HTTP/1.0\r\n')
  s1.send(b'Host: www.python.org\r\n')
  s1.send(b'\r\n')
  resp = b''.join(iter(partial(s1.recv, 8192), b''))
  with conn as s2:
    s2.send(b'GET / index.html HTTP/1.0\r\n')
    s2.send(b'Host: www.python.org\r\n')
    s2.send(b'\r\n')
    resp = b''.join(iter(partial(s2.recv, 8192), b''))

print('\n!---SECTION---\n')

