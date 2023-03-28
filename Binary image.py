import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

h = int(input())
row = []

for i in range(h):
    row.append(input().split(" "))


ss = 0
for i in range(h):
    s = 0
    for j in range(len(row[i])):
        s += int(row[i][j])
    if i == 0:
        ss = s
    elif ss != s:
        #print(ss,s, file=sys.stderr, flush=True)
        print("INVALID")
        sys.exit()


for i in range(h):
    bw = "w"
    c = ""
    #print((row[i]), file=sys.stderr, flush=True)
    for j in range(len(row[i])):
        if (row[i][j])=="0":
            bw = "b"
        else:
            if bw == "b":
                #print((row[i][j]), file=sys.stderr, flush=True)
                c+="O"*int(row[i][j])
                bw = "w"
            else:
                #print((row[i][j]), file=sys.stderr, flush=True)
                c+="."*int(row[i][j])
                bw = "b"
    print(c)

    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

