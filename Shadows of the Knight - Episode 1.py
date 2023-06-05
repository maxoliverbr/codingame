import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

print(w,h,n, file=sys.stderr, flush=True)
print(x0,y0, file=sys.stderr, flush=True)

step_w = w//2
step_h = h//2

d = {
    "D": (0,step_h),
    "U": (0,-step_h),
    "L": (-step_w,0),
    "R": (step_w,0),
    "UR": (step_w,-step_h),
    "UL": (-step_w,-step_h),
    "DR": (step_w,step_h),
    "DL": (-step_w,step_h)
}

dx0=dy0=0
i = 1
p_dir = ""
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    print("BD = ", bomb_dir, file=sys.stderr, flush=True)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    if p_dir != bomb_dir:
        if   (p_dir == "U" and bomb_dir == "D")  or (p_dir =="D" and bomb_dir=="U"):
            pass
        elif (p_dir == "U" and bomb_dir == "DR") or (p_dir =="D" and bomb_dir=="UR"):
            pass
        elif (p_dir == "U" and bomb_dir == "DR") or (p_dir =="D" and bomb_dir=="UR"):
            pass
        elif (p_dir == "U" and bomb_dir == "DR") or (p_dir =="D" and bomb_dir=="UR"):
            pass
        
        i+=1
    else:
        i=2

    dx0 = (d[bomb_dir][0])/i
    dy0 = (d[bomb_dir][1])/i

    x0 += math.floor(dx0)
    y0 += math.floor(dy0)

    if x0>=w:
        x0=w-1
    elif x0<0:
        x0=0

    if y0>=h:
        y0=h-1
    elif y0<0:
        y0=0
    
    p_dir = bomb_dir
    p_x   = x0
    p_y   = y0

    print("DD = ", dx0, dy0, file=sys.stderr, flush=True)        
    # the location of the next window Batman should jump to.
    print(f"{x0} {y0}")
    #i+=1
