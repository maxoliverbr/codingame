import sys
import math

s1 = "+---[CODINGAME]---+"
s2 = "+-----------------+"

board = [
"                 ",
"                 ",
"                 ",
"                 ",
"                 ",
"                 ",
"                 ",
"                 ",
"                 "
]


def str_replace(s,x,y):
    bl = list(board[y])
    bl[x] = s
    bl = "".join(bl)
    board[y] = bl


def get_key(my_dict, val):
    # print(val, file=sys.stderr, flush=True)
    for key, value in my_dict.items():
        if val == value:
            return key
    return -1 
 


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

fingerprint = input().split(":")

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

#print(fingerprint, file=sys.stderr, flush=True)

x = 8
y = 4


actions = {
        "00": ("upleft",-1,-1),
        "01": ("upright",-1,+1),
        "10": ("downleft",+1,-1),
        "11": ("downright",+1,+1)
}

symbols = {
    0: " ",
    1: ".",
    2: "o",
    3: "+",
    4: "=",
    5: "*",
    6: "B",
    7: "O",
    8: "X",
    9: "@",
    10: "%",
    11: "&",
    12: "#",
    13: "/",
    14: "^"
}

str_replace("S", 8, 4)

for nibble in fingerprint:
    b_nibble = bin(int(nibble,16))[2:].zfill(8)[::-1]
    for i in range(0,8,2):
        action = b_nibble[i:i+2]
        x += actions[action][1]
        y += actions[action][2]

        if x == -1 and y == -1:
            x, y = 0, 0
        elif x == 17 and y == -1:
            x, y = 16, 0
        elif x == -1 and y == 9:
            x, y = 0, 8
        elif x == 17 and y == 9:
            x, y = 16, 8
        elif x == -1 and (y >=0 and y <= 8):
            x = 0
        elif x == 17 and (y >=0 and y <= 8):
            x = 16
        elif (x >=0 and x<=16) and y == -1:
            y = 0
        elif (x >=0 and x<=16) and y == 9:
            y = 8

        
        c = board[y][x]
        
        c_key = get_key(symbols, c)
        
        if c_key == 14:
            c_key = -1

        next_c = symbols[c_key+1]
        str_replace(next_c, x, y)

        

str_replace("S", 8, 4)
str_replace("E", x, y)

print(s1)
for line in board:
    print(f"|{line}|")
print(s2)
