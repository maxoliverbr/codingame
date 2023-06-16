import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
class Registers:
    a = 0
    b = 0
    c = 0 
    d = 0
    line = 0

register = Registers()
instructions = []

register.a, register.b, register.c, register.d = [int(i) for i in input().split()]

def MOV(r,val):
    if val.isalpha():val = f"register.{val}"
    if   r == "a":register.a = eval(val)
    elif r == "b":register.b = eval(val)
    elif r == "c":register.c = eval(val)
    elif r == "d":register.d = eval(val)
    

def ADD(r, val1, val2):    
    if val1.isalpha():val1 = f"register.{val1}"
    if val2.isalpha():val2 = f"register.{val2}"
    if   r == "a":register.a = eval(val1)+eval(val2)
    elif r == "b":register.b = eval(val1)+eval(val2)
    elif r == "c":register.c = eval(val1)+eval(val2)
    elif r == "d":register.d = eval(val1)+eval(val2)

    

def SUB(r,val1,val2):
    if val1.isalpha():val1 = f"register.{val1}"
    if val2.isalpha():val2 = f"register.{val2}"
    if   r == "a":register.a = eval(val1)-eval(val2)
    elif r == "b":register.b = eval(val1)-eval(val2)
    elif r == "c":register.c = eval(val1)-eval(val2)
    elif r == "d":register.d = eval(val1)-eval(val2)
    

def JNE(imm,val1,val2):
    if val1.isalpha():val1 = f"register.{val1}"
    if val2.isalpha():val2 = f"register.{val2}"
    res_1 = eval(val1)
    res_2 = eval(val2)
   
    if res_1 != res_2:
        register.line = int(imm)-1
    

#a, b, c, d = [int(i) for i in input().split()]
n = int(input())

for i in range(n):
    instructions.append(input())

register.line = 0

while True:
    
    i = instructions[register.line].split()

    if i[0]=="MOV":
        r = eval(f"{i[0]}('{i[1]}','{i[2]}')")
    elif i[0]=="ADD" or i[0]=="SUB":
        r = eval(f"{i[0]}('{i[1]}','{i[2]}','{i[3]}')")
    elif i[0] == "JNE":
        r = eval(f"{i[0]}('{i[1]}','{i[2]}','{i[3]}')")
    
    register.line+=1
    
    if register.line>=n:
        print(register.a,register.b,register.c,register.d)
        sys.exit()
    

