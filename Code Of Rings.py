import sys
import math

magic_phrase = input()
print(len(magic_phrase), file=sys.stderr, flush=True)
print(magic_phrase, file=sys.stderr, flush=True)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
o=""
buffer = "@"*30 
ilb=mc=m=0
d="+"
a=" ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ord_m = ord("M")

for l in range(len(magic_phrase)):
    nc = ""
    c_buffer = buffer[l%30]
    
    if c_buffer == "@":
        ord_c_buffer = 64
    else:    
        ord_c_buffer = ord(c_buffer)
    
    ord_c_message = ord(magic_phrase[l])

    if c_buffer == "@" and magic_phrase[l] == " ":
        d=""
        d_ord=0
    elif magic_phrase[l] != " " and c_buffer == " ":
        d="+"
        d_ord=ord(magic_phrase[l])-64
    elif c_buffer == " " and magic_phrase[l] == " ":
        d=""
        d_ord = 0        
    elif c_buffer != " " and magic_phrase[l] == " ":
        d="+"
        d_ord = ord("Z") - ord_c_buffer + 1
    elif ord_c_buffer>ord_c_message:
        d="-"
        d_ord = ord_c_buffer - ord_c_message
    else:
        d="+"
        d_ord = ord_c_message - ord_c_buffer
    buffer = buffer[:l%30] + magic_phrase[l] + buffer[l%30+1:]
    m = d_ord
    #print(f"{l:0>3}, {l%30:0>3} '{magic_phrase[l]}' '{c_buffer}' {ord_c_buffer} {ord_c_message} m={m:0>2} {d}", file=sys.stderr, flush=True)   
    o += d*m+".>"
print(len(o), file=sys.stderr, flush=True)   
print(o)
