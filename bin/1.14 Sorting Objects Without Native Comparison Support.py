'''
Title    -  1.14 Sorting Objects without Native Comparison Support
Problem  -  Have a list of dictionaries and you would like to sort the entries
              according to one or more of the dictionary values
Solution -  Use sorted() method
'''

class User:
  def __init__(self, user_id):
    print('User.__init__')
    self.user_id = user_id
  def __repr__(self):
    print('User.__repr__')
    return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]
print('Users:', users)

# create a key by calling __repr__ method() in a lambda 
print('Sorted Users:', sorted(users, key=lambda u: u.user_id))

# use operator.atttrgetter() instead of lambda
# attrgetter() is faster than lamda
# multiple fields can be retrieved using attrgetter()
from operator import attrgetter
print('Sorted attrgetter Users:', sorted(users, key=attrgetter('user_id')))

# Can apply this to min() & max() methods()
print('Min:', min(users, key=attrgetter('user_id')))
print('Max:', max(users, key=attrgetter('user_id')))
