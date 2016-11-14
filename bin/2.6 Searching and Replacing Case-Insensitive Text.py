'''
Title    -  2.6. Searching and Replacing Case-Insensitive Text 
Problem  -  Need to earch for & possibly replace text in a case-insensitive manner  
Solution -  use re module and supply re.IGNORECASE flag to operations
'''

import re
text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))

# Need a support function to replace in the same case 
def matchcase(word):
  def replace(m):
    text = m.group()
    if text.isupper():
      return word.upper()
    elif text.lower():
      return word.lower()
    elif text[0].isupper():
      return word.capitalize()
    else:
      return word 
  return replace 
print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))

