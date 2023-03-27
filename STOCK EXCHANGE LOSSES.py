import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
v = [int(x) for x in input().split()]

vmax = 0
lmax = 0

for i in v:
    if i > vmax:
        vmax=i
    lg = i-vmax
    if lg<0 and lg<lmax:
            lmax = lg

print(lmax)
