x=o=""
for c in input():x+=format(ord(c),"07b")
D=F=False
y="0"
for i in x:
 if i=="1" and not F:
  o+=" 0 0"
  F=True
  D=False
 elif i=="1" and F:
  o+=y
 elif i==y and not D:
  o+=" 00 0"
  D=True
  F=False
 elif i==y and D:
  o+=y
print(o[1:])
