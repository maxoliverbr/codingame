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

step_w = 1/w
step_h = 1/h

d = {
    "U": (0,step_h),
    "D": (0,-step_h),
    "L": (-step_w,0),
    "R": (step_w,0),
    "UR": (step_w,step_h),
    "UL": (-step_w,step_h),
    "DR": (step_w,-step_h),
    "DL": (-step_w,-step_h)
}


# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    print("BD = ", bomb_dir, file=sys.stderr, flush=True)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    x1 = x0 + d[bomb_dir][0]
    y1 = y0 + d[bomb_dir][1]

    # the location of the next window Batman should jump to.
    print(f"{x1} {y1}")
