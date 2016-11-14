'''
Title    -  1.12 Determining the Most Frequently Occurring Items in a Sequence 
Problem  -  Have a seq of items, & like to determine most frequently occuring item 
              in the seq
Solution -  Use collections.Counter class
'''

words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]

# most_common returns a list with tuples of key: value pairs (word, # of words)
from collections import Counter 
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print('Top three:', top_three)

# Counter create dictionary mapping word to occurance
# Word is key and value is return 
print('not:', word_counts['not'])
print('eyes:', word_counts['eyes'])

print('one:', word_counts)
morewords = ['why','are','you','not','looking','in','my','eyes']
print('START--->')
for word in morewords:
  # adds 1 each word
  word_counts[word] +=1
  print(word, word_counts[word])
print('Eyes:', word_counts['eyes'])
print('two:', word_counts)

word_counts.update(morewords)
print('three:', word_counts)

a = Counter(words)
b = Counter(morewords)
# Combine counts
c = a + b
print('Add:', c)
# Subtrace counts
d = a - b
print('Sub', d)