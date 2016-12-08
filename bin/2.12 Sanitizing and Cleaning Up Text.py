'''
Title    -  2.12. Want to clean up unicode text
Problem  -  Want to strip unwanted chars, from beginning, end or middle of a text string
Solution -  Use basic string functions: str.upper(), str.lower() or simple replacements
              str.replace(), or re.sub(), or normalize text with unicodedata.normalize(),
              or use str.translate() method
'''

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

# cleanup whitespace by remapping to ' '
# requires python3
remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None  # Deleted 
}
a = s.translate(remap)
print(a)

# remove all the combining chars
import unicodedata
import sys
# maps every Unicode combining char to None and deletes the accents
# can use to delete control chars 
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                          if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chrs))

# maps all Unicode decimal digit chars to their equivalent ASCII 
digitmap = { c: ord('0') + unicodedata.digit(chr(c))
          for c in range(sys.maxunicode)
          if unicodedata.category(chr(c)) == 'Nd' }
print(len(digitmap))
# Arabic digits 
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))

# I/O decoding & encoding functions
# ascii encode / decode discards all unicode chars for ascii 
print(a)
b = unicodedata.normalize('NFD', a)
print(b.encode('ascii', 'ignore').decode('ascii'))

# sanitizing text creates issus with runtime performance
# str.replace() method runs fastest.  Even on multiple calls 
# Runs much fster than translate() or regex 
def clean_spaces(s):
  s = s.replace('\r', '')
  s = s.replace('\t', ' ')
  s = s.replace('\f', ' ') 
  return s
print(clean_spaces(s))