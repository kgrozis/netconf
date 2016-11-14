'''
Title    -  1.4 Finding the Largest or Smallest N Items
Problem  -  Want to make a list of the largest or smallest N items in a collection
Solution -  Use heapq.nlargest() or heapq.nsmallest()
'''

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # Prints 42, 37, 23
print(heapq.nsmallest(3, nums)) # Prints -4, 2, 3

# key paramter for each function to be used with more complicated data types
# nlargest and nsmallest provide superior performance
portfolio = [
   {'name': 'IBM', 'shares': 100, 'price': 91.1},
   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
   {'name': 'FB', 'shares': 200, 'price': 21.09},
   {'name': 'HPQ', 'shares': 35, 'price': 31.75},
   {'name': 'YHOO', 'shares': 45, 'price': 16.35},
   {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key= lambda s: s['price'])
print('Cheap:', cheap)
expensive = heapq.nlargest(3, portfolio, key = lambda s: s['price'])
print('Expensive:', expensive)

nums = [1,8,2,23,7,-4,18,23,42,37,2]
# heap[0] is always the smallest number in list
heap = list(nums)
heapq.heapify(heap)
print('Heap:', heap)
# heapq.heappop() method pops the smallest item in list and replaces it with next smallest
print('Heap -1:', heapq.heappop(heap))
print('Heap -2:', heapq.heappop(heap))
print('Heap -3:', heapq.heappop(heap))

