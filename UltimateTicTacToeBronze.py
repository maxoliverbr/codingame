import sys
import math
import copy

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

mainboard = [['','',''],['','',''],['','','']]


def loose(board):
    #print(board, file=sys.stderr, flush=True)
    if board[0][0]=='O' and board[1][0]=='O' and board[2][0]=='O':
        return("l")
    elif board[0][1]=='O' and board[1][1]=='O' and board[2][1]=='O':
        return("l")
    elif board[0][2]=='O' and board[1][2]=='O' and board[2][2]=='O':
        return("l")
    elif board[0][0]=='O' and board[0][1]=='O' and board[0][2]=='O':
        return("l")        
    elif board[1][0]=='O' and board[1][1]=='O' and board[1][2]=='O':
        return("l")
    elif board[2][0]=='O' and board[2][1]=='O' and board[2][2]=='O':
        return("l")
    elif board[0][0]=='O' and board[1][1]=='O' and board[2][2]=='O':
        return("l")
    elif board[0][2]=='O' and board[1][1]=='O' and board[2][0]=='O':
        return("l")

    return (None)

def win(board):
    #print(board, file=sys.stderr, flush=True)
    if board[0][0]=='X' and board[1][0]=='X' and board[2][0]=='X':
        return("w")
    elif board[0][1]=='X' and board[1][1]=='X' and board[2][1]=='X':
        return("w")
    elif board[0][2]=='X' and board[1][2]=='X' and board[2][2]=='X':
        return("w")
    elif board[0][0]=='X' and board[0][1]=='X' and board[0][2]=='X':
        return("w")        
    elif board[1][0]=='X' and board[1][1]=='X' and board[1][2]=='X':
        return("w")
    elif board[2][0]=='X' and board[2][1]=='X' and board[2][2]=='X':
        return("w")
    elif board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X':
        return("w")
    elif board[0][2]=='X' and board[1][1]=='X' and board[2][0]=='X':
        return("w")

    return (None)

def check_win(board,x,y):
    b = copy.deepcopy(board)
    b[x][y] = 'X'
    m = win(b)
    #print(board,b,m,x,y, file=sys.stderr, flush=True)
    if m=="w":
        return True
    else:
        return False

def check_loose(board,x,y):
    b = copy.deepcopy(board)
    b[x][y] = 'O'
    m = loose(b)
    #print(board,b,m,x,y, file=sys.stderr, flush=True)
    if m=="l":
        return True
    else:
        return False
    
# game loop
while True:
    valid = []
    
    opponent_row, opponent_col = [int(i) for i in input().split()]
    valid_action_count = int(input())
    print(valid_action_count, file=sys.stderr, flush=True)

    for i in range(valid_action_count):
        row, col = [int(j) for j in input().split()]
        valid.append((row,col))
    
    if opponent_col == -1 and opponent_row == -1:
        mainboard = [['','',''],['','',''],['','','']]
    else:
        mainboard[opponent_row][opponent_col] = "O"

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    

    if valid_action_count == 9:
        x,y = 1,1
        mainboard[x][y] = "X"
        print(f"{x} {y}")
    else:
        move_found = False
        for xx,yy in valid:
            print(xx,yy, file=sys.stderr, flush=True)
    
            if check_loose(mainboard,xx,yy) == True:
                mainboard[xx][yy] = "X"
                print(f"{xx} {yy}")    
                move_found = True
                break
        
            if check_win(mainboard,xx,yy) == True:
                mainboard[xx][yy] = "X"
                print(f"{xx} {yy}")    
                move_found = True
                break
        
        if move_found == False:
            x,y = valid[0]
            mainboard[x][y] = "X"
            print(f"{x} {y}")

        #else:
        #    x = int(random.random()*3)
        #    y = int(random.random()*3)
            
        #    if (x,y) in valid:
        #        mainboard[x][y] = "X"
        #        print(f"{x} {y}")
        #    else:
        #        x, y = valid[0]
        #        mainboard[x][y] = "X"
        #        print(f"{x} {y}")
                
    #print(mainboard, file=sys.stderr, flush=True)
    
    #print(opponent_col, file=sys.stderr, flush=True)
        
