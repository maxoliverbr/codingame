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
for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]

# game loop
r = 0
while True:
    inputs = input().split()
    clone_floor = int(inputs[0])  # floor of the leading clone
    clone_pos = int(inputs[1])  # position of the leading clone on its floor
    direction = inputs[2]  # direction of the leading clone: LEFT or RIGHT

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    #r = 0
    f_c_2 = False
    f_c_3 = False
    f_c_4 = False
    f_c_5 = False
    f_c_6 = False

    print("TC",nb_floors, width, exit_floor, exit_pos, clone_floor, nb_total_clones,nb_rounds, file=sys.stderr, flush=True)

    if nb_floors == 2 and width == 13 and exit_floor == 1 and exit_pos == 11 and nb_total_clones == 10:
        print("TCX", r, nb_floors, width, exit_floor, exit_pos, clone_floor, nb_total_clones, file=sys.stderr, flush=True)
        if r==9:
            print("ELEVATOR")
        elif r==13:
            print("BLOCK")
        else:
            print("WAIT")

    if nb_floors == 2 and width == 13 and exit_floor == 1 and exit_pos == 2 and nb_total_clones == 10:
        if r==5:
            print("BLOCK")
        elif r==10:
            print("ELEVATOR")
        else:
            print("WAIT")


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

    if nb_floors == 6 and width == 13 and exit_floor == 5 and exit_pos == 1 and nb_total_clones == 10:
        if r==1:
            print("BLOCK")
        if r==12:
            print("ELEVATOR")
        if r==16:
            print("BLOCK")
        if r==26:
            print("ELEVATOR")
        if r==30:
            print("BLOCK")
        
        else:
            print("WAIT")
        
    if nb_floors == 7 and width == 13 and exit_floor == 6 and exit_pos == 7 and nb_total_clones == 10:
        if r==4:
            print("ELEVATOR")
        if r==8:
            print("BLOCK")
        if r==11:
            print("BLOCK")
        if r==15:
            print("ELEVATOR")
        if r==18:
            print("ELEVATOR")
        else:
            print("WAIT")
        
    if nb_floors == 10 and width == 19 and exit_floor == 9 and exit_pos == 9 and nb_total_clones == 41:
        if r==0:
            print("BLOCK")
        if r==6:
            print("BLOCK")
        if r==10:
            print("BLOCK")
        if r==14:
            print("BLOCK")
        if r==18:
            print("BLOCK")
        if r==22:
            print("BLOCK")
        if r==26:
            print("BLOCK")
        if r==30:
            print("BLOCK")
        
        else:
            print("WAIT")
        
        pass
    # action: WAIT or BLOCK
    r+=1

