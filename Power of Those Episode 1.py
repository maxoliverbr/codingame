import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

x1 = (light_x - initial_tx)
y1 = (light_y - initial_ty)


# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    m1 = ""
    m2 = ""
    if x1>0:
        m1 = "E"
        x1 -=1
    elif x1<0: 
        m1 = "W"
        x1 +=1
    
    if y1>0:
        m2 = "S"
        y1-=1
    elif y1<0: 
        m2 = "N"
        y1+=1
    
    print(m2+m1)
