import sys
import math

"""
6 6 1 6 11
..H... ......
...... ..H...
E...G. .E.G..
...... ..F...
..F... ......
...... ......

......
......
..E...
......
......
......

"""

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h, t1, t2, t3 = [int(i) for i in input().split()]
first_picture_row=[]
second_picture_row=[]
asteroids = []
output = [(["."]*w) for i in range(h)]

dt21 = t2-t1
dt32 = t3-t2
print(dt32,dt21, file=sys.stderr, flush=True)

for i in range(h):
    f_row, s_row = input().split()
    first_picture_row.append(f_row)
    second_picture_row.append(s_row)
    for j in f_row:
        if j!=".":
            asteroids.append([j,-1,-1])
asteroids = sorted(asteroids,reverse=True)
print(asteroids, file=sys.stderr, flush=True)

for asteroid in asteroids:
    xy_second, xy_first = [-1,-1],[-1,-1]
    for i in range(w):
        for j in range(h):
            if first_picture_row[i][j] == asteroid[0]:
                xy_first = [i,j]
                #print("xy_first=",xy_first, file=sys.stderr, flush=True)
            if second_picture_row[i][j] == asteroid[0]:
                xy_second = [i,j]
                #print("xy_second=",xy_second, file=sys.stderr, flush=True)
                
            if xy_first!=[-1,-1] and xy_second!=[-1,-1]:
                tx = (xy_second[0]-xy_first[0])/dt21
                ty = (xy_second[1]-xy_first[1])/dt21

                cx = math.floor(xy_second[0]+tx*dt32)
                cy = math.floor(xy_second[1]+ty*dt32)
                print(cx,cy, file=sys.stderr, flush=True)
                output[cx][cy] = asteroid[0]
                
                
#print(output, file=sys.stderr, flush=True)
           
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for i in output:
    print(''.join(map(str, i)))
