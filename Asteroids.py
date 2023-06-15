import sys
import math

w, h, t1, t2, t3 = [int(i) for i in input().split()]
first_picture_row=[]
second_picture_row=[]
asteroids = []
output = [(["."]*w) for i in range(h)]

dt21 = t2-t1
dt32 = t3-t2

for i in range(h):
    f_row, s_row = input().split()
    first_picture_row.append(f_row)
    second_picture_row.append(s_row)
    for j in f_row:
        if j!=".":
            asteroids.append(j)
asteroids = sorted(asteroids,reverse=True)

for asteroid in asteroids:
    xy_second, xy_first = [None,None],[None,None]
    for i in range(w):
        for j in range(h):
            if first_picture_row[i][j] == asteroid[0]:
                xy_first = [i,j]
                
            if second_picture_row[i][j] == asteroid[0]:
                xy_second = [i,j]
                
            if xy_first!=[None,None] and xy_second!=[None,None]:
                tx = (xy_second[0]-xy_first[0])/dt21
                ty = (xy_second[1]-xy_first[1])/dt21

                cx = math.floor(xy_second[0]+tx*dt32)
                cy = math.floor(xy_second[1]+ty*dt32)
                
                if 0<=cx<w and 0<=cy<h:
                    output[cx][cy] = asteroid[0]

for i in output:
    print(''.join(map(str, i)))
