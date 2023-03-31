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

