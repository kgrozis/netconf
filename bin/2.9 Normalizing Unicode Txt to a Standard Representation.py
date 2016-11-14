'''
Title    -  2.9. Normalizing Unicode Text to a Standard Representation
Problem  -  Working with Unicode strings, but need to make sure that all of the strings have 
              the same underlying representation
              In Unicode certain chars can be represented by more than one valid seq of code points
Solution -  
'''

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
# 2 strings do not compare because diff unicode chars 
print(s1 == s2)
print(len(s1))
print(len(s2))

# Normalize the text into standard representation using unicodedata module 
import unicodedata
# specifies how you want string normalized
# NFC means chars should be fully composed  - single code point 
# NFD means chars should be fully decomposed - combining chars 
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
# Strings normalized 
print(t1 == t2)
print(ascii(t1))

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4)
print(ascii(t3))

s = '\ufb01'    # a single char 
print(s)
print(unicodedata.normalize('NFD', s))
# Adds extra chars for dealing with certain kinds of chars 
print(unicodedata.normalize('NFKD', s))
print(unicodedata.normalize('NFKC', s))

# important when processing strings you don't have control of
t1 = unicodedata.normalize('NFD', s1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))
