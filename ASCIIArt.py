import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input().upper()
row  = []
for i in range(h):
    row.append(input())

s = [""]*h
#print(t, file=sys.stderr, flush=True)

for i in t:
    #print(i, file=sys.stderr, flush=True)
    if i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ?":
        c = l*26
    else:
        c = l*(ord(i)-65)
    #print(c, file=sys.stderr, flush=True)
    for i in range(h):
        s[i] = s[i] + (row[i][0+c:l+c])

for i in range(h):
    print(s[i])


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
