import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def find_a(m):
    start = []
    for i in range(len(m[0])):
        for j in range(len(m[0])):
            if m[i][j] == "a":
                start.append((i,j))
    return start

def scan_next(x,y,m,c):
    s = len(m[0])

    if x-1>=0 and m[x-1][y]==c:
        return x-1,y
    elif x+1<s and m[x+1][y]==c:
        return x+1,y
    elif y-1>=0 and m[x][y-1]==c:
        return x,y-1
    elif y+1<s and m[x][y+1]==c:
        return x,y+1
    
    return -1,-1

def str_replace(board,s,x,y):
    bl = list(board[y])
    bl[x] = s
    bl = "".join(bl)
    board[y] = bl

n = int(input())
m = []
for i in range(n):
    m.append(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

x, y = 0, 0

solution = False

solution_path = []

start = find_a(m)
#print(start, file=sys.stderr, flush=True)
head = "a"

#for i in range(n):
#    print(m[i], file=sys.stderr, flush=True)

for path_start in start:
    x0, y0 = path_start
    solution_path.append((x0,y0))
    while solution == False:
        c = chr(ord(head)+1)
        nextx, nexty = scan_next(x0,y0,m,c)
        if nextx == -1 and nexty == -1:
            start.remove(path_start)
            #print(c, nextx, nexty, file=sys.stderr, flush=True)
            head = "a"
            solution_path =[]
            break
        else:
            solution_path.append((nextx,nexty))
            head = c
            if c == "z":
                solution = True
            x0, y0 = nextx, nexty
        #print(c, nextx, nexty, file=sys.stderr, flush=True)

# print(start, solution_path)

o = []
for i in range(n):
    o.append("-"*n)

c = "a"
for i in solution_path[0:26]:
    x,y = i
    print(x,y,c, file=sys.stderr, flush=True)
    str_replace(o,c,y,x)
    c = chr(ord(c)+1)

for i in range(n):
    print(o[i])

