import sys

n = int(input())
a = input()

lena = len(a)
n+=1
ss = ""
while n>0:
    r = n%lena-1
    if r<0:
        r=lena-1
    cc = a[r]
    ss+=cc
    n = (n-r)//lena
print(ss)

"""

abcdabcdabcdabcdabcdabcdabcdabcd
a
    a
        a
            a
  a  =  0,   b = 1,  c =  2,   d = 3
 aa  =  4,  ba = 5, ca =  6,  da = 7
 ab  =  8,  bb = 9, cb = 10, db = 11
...
aaa   = 20, baa = 21, caa = 22, daa = 23
    a  = a         0
   aa  = a + a     4 =  4 + 0
  aaa  = a + aa   20 = 16 + aa
 aaaa  = a + aaa  x  = 4^3  + 20 = 84
baaaa = 26^(4)+ 84+1

"""
