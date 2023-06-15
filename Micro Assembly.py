import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
class Registers:
    a = 0
    b = 0
    c = 0 
    d = 0

register = Registers()

register.a, register.b, register.c, register.d = [int(i) for i in input().split()]
print(register.a,register.b,register.c,register.d, file=sys.stderr, flush=True)

def MOV(r,val):
    print(f"{r}, val ",r, val, file=sys.stderr, flush=True)
    
    if val.isalpha():val = f"register.{val}"
    if   r == "a":register.a = eval(val)
    elif r == "b":register.b = eval(val)
    elif r == "c":register.c = eval(val)
    elif r == "d":register.d = eval(val)
    

def ADD(reg, val1, val2, val3):
    pass

def SUB(reg,val):
    pass

def JNE(imm,val1,val2):
    pass


#a, b, c, d = [int(i) for i in input().split()]
n = int(input())
instructions = []
for i in range(n):
    instructions.append(input())

for instruction in instructions:
    print(register.a,register.b,register.c,register.d, file=sys.stderr, flush=True)
    i = instruction.split()

    #if i[1]=="a": i[1]= "register.a"
    #if i[2]=="a": i[2]= "register.a"
    #print(f"{c[0]} {c[1]} {c[2]}", file=sys.stderr, flush=True)
    print((f"func = {i[0]}({i[1]},{i[2]})"), file=sys.stderr, flush=True)

    r = eval(f"{i[0]}('{i[1]}','{i[2]}')")
    #print(instruction.split(), file=sys.stderr, flush=True)
print(register.a,register.b,register.c,register.d)


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


