import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

o = ""
x = ""
z = ""

for c in message:
    x += format(ord(c),"07b")
   
First1 = False
First0 = False

for i in x:
    if i == "1" and not First1:
        o += " 0 0"
        First1 = True
        First0 = False
    elif i =="1" and First1:
        o += "0"
    elif i =="0" and not First0:
        o += " 00 0"
        First0 = True
        First1 = False
    elif i == "0" and First0:
        o += "0"
print(o.strip())

