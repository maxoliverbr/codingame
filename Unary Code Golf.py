x=o=""
for c in input():x+=format(ord(c),"07b")
d=e=0
for i in x:
 if i=="1" and not e:e,d,o=1,0,o+" 0 0"
 elif i=="0" and not d:d,e,o=1,0,o+" 00 0"
 else:o+="0"
print(o[1:])
