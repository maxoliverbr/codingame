import sys
import math

"""
GUZ MUG ZOG GUMMOG ZUMGUM ZUM MOZMOZ MOG ZOGMOG GUZMUGGUM
GUZ MUG ZOG GUMMOG ZUMGUM ZUM MOZMOZ MOG ZOHMOG GUZMUHGUM
12345678901234567890123456789012345678901234567890
                                           X
"""
oo=""

def calc_moves(buf:str,magic:str): 
    a=" ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c="012345678901234567890123456"
    diff=0
    dir=""
    c_buffer = a.find(buf)
    c_magic  = a.find(magic)
    diff = abs(c_buffer-c_magic)
    d = c_buffer-c_magic
    
    print(f"'ZZZZ' {buf} {magic}", file=sys.stderr, flush=True)    
    if diff>13:
        diff=26-diff+1
        dir = "-"
    elif c_buffer>c_magic:
        print(f"'YYYY' {buf} {magic}", file=sys.stderr, flush=True)    
        if buf=="U" and magic=="G":
            print(f"'XXXX'", file=sys.stderr, flush=True)    
            diff+=1
        dir = "-"
    else:
        dir = "+"
        print(f"'EEEE' {buf} {magic} {dir}", file=sys.stderr, flush=True)    
    
    #print(f"'{buffer}' '{magic}' c_buffer={c_buffer:>02} c_magic={c_magic:>02} diff={diff:>02} {dir} d={d} ", file=sys.stderr, flush=True)    
    
    #print(f">>>> '{diff}' '{buf}' {c_buffer} '{magic}' {c_magic} '{dir}'", file=sys.stderr, flush=True)    
    return (dir,diff)
    
    #print(f"'{buffer}' '{magic}' '{c}' {c_buffer:>02} {c_magic:>02} {diff:>02} {dir} ", file=sys.stderr, flush=True)    


magic_phrase = input()
print(len(magic_phrase), file=sys.stderr, flush=True)
print(magic_phrase, file=sys.stderr, flush=True)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
o=""
buffer = " "*30 
ilb=mc=m=0
d="+"

ord_m = ord("M")

for l in range(len(magic_phrase)):
    nc = ""
    c_buffer = buffer[l%30]
    
    xx,yy = calc_moves(c_buffer,magic_phrase[l])
    oo+=xx*yy+".>"

    if c_buffer == " ":
        ord_c_buffer = 64
    else:    
        ord_c_buffer = ord(c_buffer)
    
    ord_c_message = ord(magic_phrase[l])

    if c_buffer == " " and magic_phrase[l] == " ":
        d=""
        d_ord=0
    elif magic_phrase[l] != " " and c_buffer == " ":
        d="+"
        d_ord=ord(magic_phrase[l])-64      
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
print(len(oo), file=sys.stderr, flush=True)   
print(oo)
#print("+.--.")
