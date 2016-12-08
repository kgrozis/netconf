'''
Title    -  6.2 Reading & Writing JSON Data 
Problem  -  Want to read or write data encoded as JSON 
Solution -  Use json module. 2 main functions:
              json.dumps()
              json.loads() 
'''

import json 
# turn dict into json 
data = {
   'name' : 'ACME',
   'shares' : 100,
   'price' : 542.23
}
json_str = json.dumps(data)
print(json_str)
# turn json into dict 
data = json.loads(json_str)
print(data)

# working with files 
with open('data.json', 'w') as f:
  json.dump(data, f)
# reading data back 
with open('data.json', 'r') as f:
  data = json.load(f)

# Not all python syntax maps 1:1 in json 
# json module provides translation 
print(json.dumps(False))
d = {'a': True,
     'b': 'Hello',
     'c': None}
print(json.dumps(d))

# deep level of nesting in json data structs
# pprint() alphatizes keys and prints dicts in a sanier way
# from urllib.request import urlopen
# import json 
# u = urlopen('http://www.cisco.com')
# resp = json.loads(u.read().decode('utf-8'))
# from pprint import pprint 
# pprint(resp)

# preserving order in dict 
s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)

# autoformat with indent 
print(json.dumps(data))
print(json.dumps(data, indent=4))

# sort-keys on output 
print(json.dumps(data, sort_keys=True))

# turn JSON dict into Python obj 
class JSONObject:
  def __init__(self, d):
    print('JSON.__init__()')
    self.__dict__ = d
# pass JSON data as a single arg to __init__()
data = json.loads(s, object_hook=JSONObject)
print(data.name)

# instances are not normally serializable as JSON 
class Point:
  def __init__(self, x, y):
    self.x = x 
    self.y = y 
p = Point(2,3)
# fails!
# json.dumps(p)

# to serialize 
# supply function that takes an instance as input & returns a dict that can be serialized 
def serialize_instance(obj):
  d = { '__classname__':type(obj).__name__}
  d.update(vars(obj))
  return d 
p = Point(2,3)
s = json.dumps(p, default=serialize_instance)
print(s)
# to desrialize 
def unserialize_object(d):
  clsname = d.pop('__classname__',None)
  if clsname:
    cls = classes[clsname]
    obj = cls.__new__(cls) # Make instance without calling __init__ 
    for key, value in d.items:
      setattr(obj, key, value)
      return obj 
  else:
    return d
a = json.loads(s, object_hook=unserialize_object)
print(a)
