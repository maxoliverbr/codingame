# Cool clashes !

"""
x = input()

print(int(x[0]) * sum([int(i) for i in x[1:]]))
"""

"""
s = input()
l = len(s)
print(sum(map(ord,s))//l)
"""

"""
s = input()
ans = ''
for c in s:
    ans += c
    if c.isalpha():
        ans += c.swapcase()
print(ans)
"""

"""
s = input()
x=''
for i in s:
    if i.isupper():
        x+=i
print(x)
"""

"""
format (000) 000-0000
print(f"({s[:3]}) {s[3:6]}-{s[6:10]}")
"""

"""

s = input()
M = {c: s.count(c) for c in s}

for c in sorted(M.keys()):
    print(c*M[c])
    
"""

"""
_sum = input()

# Define the original string
# Split the string into a list of numbers
numbers = _sum.split("+")
numbers.sort()
sorted_string = "+".join(numbers)
print(sorted_string)

"""

"""
ROT13.5
import string as s
a=s.ascii_letters
b='0123456789'
v=input()
r=''
for c in v:
 if c in a:
  r+=a[((a.find(c)+13)%26)+(26 if c.isupper() else 0)]
 elif c in b:
  r+=b[(b.find(c)+5)%10]
 else:
  r+=c
print(r)
"""

"""
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

line = input().split()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
for l in line:
 print(sum(map(ord,l)))
"""
