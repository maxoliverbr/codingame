x=o=""
for c in input():x+=format(ord(c),"07b")
D=E=F=False
T=True
for i in x:
 if i=="1" and not E:
  o+=" 0 0"
  E=T
  D=F
 elif i=="0" and not D:
  o+=" 00 0"
  D=T
  E=F
 else:
  o+="0"
print(o[1:])
