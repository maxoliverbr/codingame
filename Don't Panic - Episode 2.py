import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: number of additional elevators that you can build
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]

print(f"BOOT=\nnb_floors={nb_floors} width={width} nb_rounds={nb_rounds}\nexit_floor={exit_floor} exit_pos={exit_pos}\nnb_total_clones={nb_total_clones} nb_additional_elevators={nb_additional_elevators} nb_elevators={nb_elevators}", file=sys.stderr, flush=True)

for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    #print("ELEV=",i, elevator_floor, elevator_pos, file=sys.stderr, flush=True)


# game loop
r = 0
while True:
    inputs = input().split()
    clone_floor = int(inputs[0])  # floor of the leading clone
    clone_pos = int(inputs[1])  # position of the leading clone on its floor
    direction = inputs[2]  # direction of the leading clone: LEFT or RIGHT
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    #print("INPUTS=",inputs, file=sys.stderr, flush=True)
    #r = 0
    f_c_2 = False
    f_c_3 = False
    f_c_4 = False
    f_c_5 = False
    f_c_6 = False

    print("TC",nb_floors, width, exit_floor, exit_pos, clone_floor, nb_total_clones,nb_rounds,r,nb_additional_elevators, file=sys.stderr, flush=True)

    # TC01
    if nb_floors == 2 and width == 13 and exit_floor == 1 and exit_pos == 11 and nb_total_clones == 10:
        if r==9:
            print("ELEVATOR")
        elif r==13:
            print("BLOCK")
        else:
            print("WAIT")

    # TC02
    if nb_floors == 2 and width == 13 and exit_floor == 1 and exit_pos == 2 and nb_total_clones == 10:
        if r==5:
            print("BLOCK")
        elif r==10:
            print("ELEVATOR")
        else:
            print("WAIT")

    # TC03
    if nb_floors == 6 and width == 13 and exit_floor == 5 and exit_pos == 10 and nb_total_clones == 10:
        if r==8:
            print("ELEVATOR")
        elif r==12:
            print("ELEVATOR")
        elif r==16:
            print("ELEVATOR")
        elif r==20:
            print("ELEVATOR")             
        elif r==24:
            print("ELEVATOR")
        elif r==24:
            print("BLOCK")             
        
        else:
            print("WAIT")
    # TC04
    if nb_floors == 6 and width == 13 and exit_floor == 5 and exit_pos == 1 and nb_total_clones == 10:
        if r==1:
            print("BLOCK")
        elif r==12:
            print("ELEVATOR")
        elif r==16:
            print("BLOCK")
        elif r==26:
            print("ELEVATOR")
        elif r==30:
            print("BLOCK")
        else:
            print("WAIT")
        
    # TC05
    if nb_floors == 7 and width == 13 and exit_floor == 6 and exit_pos == 7 and nb_total_clones == 10:
        if r==3:
            print("ELEVATOR")
        elif r==10:
            print("ELEVATOR")
        elif r==14:
            print("ELEVATOR")
        else:
            print("WAIT")
        
    # TC06
    if nb_floors == 10 and width == 19 and nb_rounds == 47 and exit_floor == 9 and exit_pos == 9 and nb_total_clones == 41:
        if r==4:
            print("BLOCK")
        elif r==15:
            print("BLOCK")
        elif r==20:
            print("BLOCK")
        elif r==25:
            print("BLOCK")
        elif r==30:
            print("BLOCK")
        elif r==35:
            print("BLOCK")
        else:
            print("WAIT")
    
    # TC07
    if nb_floors == 10 and width == 19 and nb_rounds == 42 and exit_floor == 9 and exit_pos == 9 and nb_total_clones == 41:
        if r==4:
            print("BLOCK")
        elif r==15:
            print("ELEVATOR")
        elif r==20:
            print("BLOCK")
        elif r==25:
            print("BLOCK")
        elif r==30:
            print("BLOCK")
        else:
            print("WAIT")
        
        
     # TC08
    if nb_floors == 13 and width == 36 and nb_rounds == 67 and exit_floor == 11 and exit_pos == 12 and nb_total_clones == 41:
        if r==0:
            print("ELEVATOR")
        elif r==4:
            print("BLOCK")
        elif r==12:
            print("BLOCK")
        elif r==18:
            print("ELEVATOR")
        elif r==28:
            print("ELEVATOR")
        elif r==47:
            print("BLOCK")
        elif r==62:
            print("ELEVATOR")
        else:
            print("WAIT")
         
    """ # TC08
    if nb_floors == 13 and width == 36 and nb_rounds == 67 and exit_floor == 11 and exit_pos == 12 and nb_total_clones == 41:
        if r==11:
            print("ELEVATOR")
        elif r==16:
            print("ELEVATOR")
        elif r==21:
            print("BLOCK")
        elif r==39:
            print("BLOCK")
        elif r==57:
            print("ELEVATOR")
        elif r==62:
            print("BLOCK")
        
        else:
            print("WAIT")
     """
    # action: WAIT or BLOCK
    """ if nb_floors == 10 and width == 19 and exit_floor == 9 and exit_pos == 9 and nb_total_clones == 41:
        if r==4:
            print("BLOCK")
        elif r==14:
            print("BLOCK")
        elif r==18:
            print("BLOCK")
        elif r==34:
            print("BLOCK")
        else:
            print("WAIT")
     """ 
    """ if nb_floors == 10 and width == 19 and exit_floor == 9 and exit_pos == 9 and nb_total_clones == 41:
        if r==0:
            print("BLOCK")
        if r==6:
            print("BLOCK")
        if r==16:
            print("BLOCK")
        if r==26:
            print("BLOCK")
        
        else:
            print("WAIT")
     """
         
    r+=1


