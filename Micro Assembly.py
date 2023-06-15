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
    

def ADD(r, val1, val2):
    print(f"{r}, val1, val2 ",r, val1,val2, file=sys.stderr, flush=True)
    if val1.isalpha():val1 = f"register.{val1}"
    if val2.isalpha():val2 = f"register.{val2}"
    if   r == "a":register.a = eval(val1)+eval(val2)
    elif r == "b":register.b = eval(val1)+eval(val2)
    elif r == "c":register.c = eval(val1)+eval(val2)
    elif r == "d":register.d = eval(val1)+eval(val2)
    

def SUB(r,val1,val2):
    print(f"{r}, val1, val2 ",r, val1,val2, file=sys.stderr, flush=True)
    if val1.isalpha():val1 = f"register.{val1}"
    if val2.isalpha():val2 = f"register.{val2}"
    if   r == "a":register.a = eval(val1)-eval(val2)
    elif r == "b":register.b = eval(val1)-eval(val2)
    elif r == "c":register.c = eval(val1)-eval(val2)
    elif r == "d":register.d = eval(val1)-eval(val2)
    

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

    if i[0]=="MOV":
        r = eval(f"{i[0]}('{i[1]}','{i[2]}')")
    elif i[0]=="ADD" or i[0]=="SUB":
        r = eval(f"{i[0]}('{i[1]}','{i[2]}','{i[3]}')")

    #print(instruction.split(), file=sys.stderr, flush=True)
print(register.a,register.b,register.c,register.d)


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


