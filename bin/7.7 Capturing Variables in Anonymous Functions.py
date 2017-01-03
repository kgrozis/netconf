'''
Title    -  Capturing Variables in Anonymous Function   
Problem  -  Defined anonymous function using lambda 
            Need to capture teh values of variables at time of def 
'''

# x is a free variable 
#   is bound at runtime, not definition time 
#   is the value at execution (20)
x = 10
a = lambda y: x + y 
x = 20 
b = lambda y: x + y 
print(a(10))
print(b(10))

print('\n!---SECTION---\n')

x = 15
print(a(10))
x = 3
print(a(10))

print('\n!---SECTION---\n')

# want anonymous func to capture a value at point of def & keep it 
# include the value as defualt value 
x = 10
a = lambda y, x=x: x+y 
x = 20 
b = lambda y, x=x: x+y 
print(a(10))
print(b(10))

print('\n!---SECTION---\n')

# lambda does not retain value 
funcs = [lambda x: x+n for n in range(5)]
for f in funcs:
  print(f(0))

# lambda retains value 
funcs = [lambda x, n=n: x+n for n in range(5)]
for f in funcs:
  print(f(0))