'''
Title    -  Encapsulating Names in a Class   
Problem  -  Want to encapsulate private data on instances of a class 
            Concerned about Python's lack of access control 
'''

# single leading underscore (_)
# programmers are expected to observe naming conventions concerning the intended usage of data & methods 
# single leading underscore (_) should always be assumed to be internal implementation 
# No language feature to encapsulate data 
class A: 
  def __init__(self):
    self._internal = 0      # An internal attribute
    self.public = 1         # A public attribute 
    print(type(self).__name__ + '.__init__()')
  def __repr__(self):
    print('< class: ' + type(self).__name__ + ' - state: var _internal: {}, var public: {} >'.format(str(self._internal), str(self.public)))
  def __str__(self):
    print('< class: ' + type(self).__name__ + ' - state: var _internal: {}, var public: {} >'.format(str(self._internal), str(self.public)))
  def public_method(self):
    '''
    Public method
    '''
    print(type(self).__name__ + '.public_method()')
  def _internal_method(self):
    '''
    Private method
    '''
    print(type(self).__name__ + '._internal_method()')

a = A()
a.public_method()
# python won't prevent access to private method
# since it's private may result in fragile code
a._internal_method()
# print(a)

print('\n!---SECTION---\n')

# double leading underscores (__), aka 'dunder' 
# creates name managling & method is renamed 
# cannot be overwritten by inheritence 
class B:
  def __init__(self):
    self.__private = 0
    print(type(self).__name__ + '.__init__()')
  def __repr__(self):
    print('< class: ' + type(self).__name__ + ' - state: var __private: {} >'.format(self.__private))
  def __private_method(self):
    print(type(self).__name__ + '.__private_method()')
  def public_method(self):
    print(type(self).__name__ + '.public_method()')
    # call internally, no name managling 
    self.__private_method()

b = B()
b.public_method()
# can't call because of name managling
# b.__private_method()
# print(b)


print('\n!---SECTION---\n')

# if you want to create a var that classes with a reserved word
# correct ettique is to use a trailing underscore 
lambda_ = 2.0 
