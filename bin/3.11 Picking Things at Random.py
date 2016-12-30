'''
Title    -  Picking Things at Random 
Problem  -  pick random items out-of-seq or generate random numbers 
'''

# random module 

# random.choice() 
# Picks a random item out of a seq 
import random
values = [1,2,3,4,5,6]
print('1:',random.choice(values))
print('2:',random.choice(values))
print('3:',random.choice(values))
print('4:',random.choice(values))
print('5:',random.choice(values))

print('\n!---SECTION---\n')

# random.sample()
# selected items are removed from further consideration
print('1:',random.sample(values, 2))
print('2:',random.sample(values, 2))
print('3:',random.sample(values, 3))
print('4:',random.sample(values, 3))

print('\n!---SECTION---\n')

# random.shuffle
# want to shuffle items in a seq 
random.shuffle(values)
print('1:',values)
random.shuffle(values)
print('2:',values)

print('\n!---SECTION---\n')

# random.randint()
# create random integers
print('1:',random.randint(0,10))
print('2:',random.randint(0,10))
print('3:',random.randint(0,10))
print('4:',random.randint(0,10))
print('5:',random.randint(0,10))

print('\n!---SECTION---\n')

# random.random()
# create random floating-point values 
print('1:',random.random())
print('2:',random.random())
print('3:',random.random())

print('\n!---SECTION---\n')

# random.getrandbits()
# Get N random-bits expressed as an integer
print('1:',random.getrandbits(200))

print('\n!---SECTION---\n')

# random.seed()
# random computes random numbers using Mersenne Twister Algo 
# can alter initial seed 
random.seed()             # seed based on system time or os.urandom()
random.seed(12345)        # seed based on integer given
random.seed(b'bytedata')  # seed based on byte data