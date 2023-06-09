import sys
import math
"""
UMNE TALMAR RAHTAINE NIXENEN UMIR
GUZ MUG ZOG GUMMOG ZUMGUM ZUM MOZROZVROGVDOGMOGVLUZMUGGZM
1234567890123456789012345678901234567890
"""

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

magic_phrase = input()
print(magic_phrase, file=sys.stderr, flush=True)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
o=""
buffer = "@"*30 
ilb=mc=m=0
d="+"
for l in range(len(magic_phrase)):
    nc = ""
    lb = buffer[l%30]
    #if lb == "A":
    #    buffer = buffer[:(l%30)] + magic_phrase[l] + buffer[l%30+1:]
    #    mc = ord(magic_phrase[l])-64
    #    m = mc
    #else:
    c_buffer = buffer[l%30]
    ord_c_buffer = ord(c_buffer)
    ord_c_message = ord(magic_phrase[l])
    if ord_c_buffer>ord_c_message:
        d="-"
        d_ord = ord_c_buffer - ord_c_message
    else:
        d="+"
        d_ord = ord_c_message - ord_c_buffer
    buffer = buffer[:l%30] + magic_phrase[l] + buffer[l%30+1:]
    m = d_ord
    #print(f"{l}, {l%30} '{magic_phrase[l]}' '{buffer[l%30]}' {ord_c_buffer} {ord_c_message} m={m} {d} {c_buffer}", file=sys.stderr, flush=True)   
    lb = buffer[l%30]
    #print(f"{l}, {l%30} '{magic_phrase[l]}' '{buffer[l%30]}' ilb={ilb} m={m} mc={mc} {ilb} {d}", file=sys.stderr, flush=True)
    o += d*m+".>"
print(len(o), file=sys.stderr, flush=True)
print(buffer, file=sys.stderr, flush=True)

print(o)
