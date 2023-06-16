import sys
import math

"""
Line 1 : An integer K representing the length of the Input Data array
Line 2 : K integers separated by white spaces representing your Input Data
Line 3 : An integer N representing the number of lines of code
Next N lines : A Line of 

tc01:
input:
1
2
1
mov x0 x1

expected:
2

tc02:
input:
2
1 2
2
mov x0 x1
mov x0 x1

output:
1 2

tc03:
2
1 2
4
mov x0 dat
mov x0 x1
mov dat acc
mov acc x1

2 1
"""

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
class CPU:
    dat = 0 # temp storage
    acc = 0 # store result arithmetric instruction
    x0  = [] # input
    x1  = [] # output

instructions = []
my_cpu = CPU()


def MOV(x,y):
    if x == "X0" and y=="X1": my_cpu.x1.append(my_cpu.x0.pop(0))
    if x == "X0" and y=="DAT": my_cpu.dat=my_cpu.x0.pop(0)
    if x == "DAT" and y=="ACC": my_cpu.acc=my_cpu.dat
    if x == "ACC" and y=="X1": my_cpu.x1.append(my_cpu.acc)
    pass

def ADD(x):
    pass

def SUB(x):
    pass

def MUL(x):
    pass

def NOT():
    pass

def DGT(x):
    pass

def DST(x):
    pass

def TEQ(x,y):
    pass

def TGT(x,y):
    pass

def TLT(x,y):
    pass

def TCP(x,y):
    pass

k = int(input())
for i in input().split():
    my_cpu.x0.append(int(i))

n = int(input())
for i in range(n):
    instructions.append(input().upper())

print(my_cpu.x0, file=sys.stderr, flush=True)
print(instructions, file=sys.stderr, flush=True)

for instruction in instructions:
    i = instruction.split()
    r = eval(f"{i[0]}('{i[1]}','{i[2]}')")

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(*my_cpu.x1)
