import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

order = input()
side = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

lr=ll=ld=lu=1
f=0
if order[-1]==side:
    print(1)
else:
    for i in order:
        f+=1
        if i=="U":
            lr=lr*2
            ll=ll*2
            lu=lu+ld
            ld=1
        if i=="D":
            lr=lr*2
            ll=ll*2
            ld=lu+ld
            lu=1
        if i=="L":
            ll=ll+lr
            lr=1
            lu=lu*2
            ld=ld*2
        if i=="R":
            lr=lr+ll
            ll=1
            lu=lu*2
            ld=ld*2
        print(f"ND={f} D={i} R={lr} L={ll} U={lu} D={ld}", file=sys.stderr, flush=True)


    if side =="R":
        print(ll)

    if side =="L":
        print(lr)

    if side =="U":
        print(ld)

    if side =="D":
        print(lu)
