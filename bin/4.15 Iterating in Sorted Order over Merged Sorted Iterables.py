'''
Title    -  Iterating in Sorted Order over Merged Sorted Iterables  
Problem  -  Have a collection of sorted seqs
            Want to iterte over a sorted seq of tem all  
'''

# heapq.merge()  
import heapq 
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a,b):
  print(c)

print('\n!---SECTION---\n')

# heapq
# never reads any supplied seqs all at once 
# can use on very long seq with very little overhead
import heapq

print('\n!---SECTION---\n')
