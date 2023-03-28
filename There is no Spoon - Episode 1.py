import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
line = []

for i in range(height):
    line.append(input())  # width characters, each either 0 or .

print(width, height, line, file=sys.stderr, flush=True)

o = ""

stack = []

for i in range(width):
    for j in range(height):
        if line[j][i] == "0":
            stack.append((j,i))

#print(stack, file=sys.stderr, flush=True)

for z in range(len(stack)):
    x,y = stack[z]
    o = f"{y} {x} "
    cell_found = False
    for i in range(y+1,width):
        #print("Fi",x,y,i, file=sys.stderr, flush=True)
        if line[x][i]=="0":
            cell_found = True
            break
        else:
            cell_found = False
    if cell_found:
        o += f"{i} {x} "
    else:
        o += "-1 -1 "
    print("Oi",o, file=sys.stderr, flush=True)
    cell_found = False
    for j in range(x+1,height):
        #print("Fj",x,y,j, file=sys.stderr, flush=True)
        if line[j][y]=="0":
            cell_found = True
            
            break
        else:
            cell_found = False
    if cell_found:
        o += f"{y} {j}"
    else:
        o += "-1 -1"            
    #print("Oj",o, file=sys.stderr, flush=True)
    #print(o, file=sys.stderr, flush=True)
    print(o)
    #print(x,y, file=sys.stderr, flush=True)


#print(stack, file=sys.stderr, flush=True)


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# Three coordinates: a node, its right neighbor, its bottom neighbor

