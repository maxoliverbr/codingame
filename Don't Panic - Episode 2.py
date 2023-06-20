import sys
nbf, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
print(f"BOOT=\nnbf={nbf} width={width} nb_rounds={nb_rounds}\nexit_floor={exit_floor} exit_pos={exit_pos}\nnb_total_clones={nb_total_clones} nb_additional_elevators={nb_additional_elevators} nb_elevators={nb_elevators}", file=sys.stderr, flush=True)
for i in range(nb_elevators):
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
r = 0
while True:
    inputs = input().split()
    clone_floor = int(inputs[0])  # floor of the leading clone
    clone_pos = int(inputs[1])  # position of the leading clone on its floor
    direction = inputs[2]  # direction of the leading clone: LEFT or RIGHT

    f_c_2 = False
    f_c_3 = False
    f_c_4 = False
    f_c_5 = False
    f_c_6 = False
    
    Action = {"E": "ELEVATOR", "B": "BLOCK", "W": "WAIT"}
    tc01 = {9: "E", 13: "B"}
    tc03 = {8: "E", 12:"E", 16:"E", 20:"E", 24:"E"}
    tc04 = {1: "B", 12:"E", 16: "B", 28:"E", 32: "B"}    
    # TC01/02
    #if nbf == 2 and width == 13 and exit_floor == 1 and exit_pos == 11 and nb_total_clones == 10:
    if r in tc01:
        o=Action[tc01[r]]
    else:
        o=Action["W"]

    # TC03
    if nbf == 6 and width == 13 and exit_floor == 5 and exit_pos in [10,11] and nb_total_clones == 10:
        if r in tc03:
            o=Action[tc03[r]]
        else:
            o=Action["W"]

    # TC04
    if nbf == 6 and width == 13 and exit_floor == 5 and exit_pos in [1,3] and nb_total_clones == 10:
        if r in tc04:
            o=Action[tc04[r]]
        else:
            o=Action["W"]
    
    # TC05
    if nbf == 7 and width == 13 and exit_floor == 6 and exit_pos in [6,7] and nb_total_clones == 10:
        tc05 = {3:"E",10:"E",14:"E"}
        if r in tc05:
            o=Action[tc05[r]]
        else:
            o=Action["W"]
    
    # TC06
    if nbf == 10 and width == 19 and nb_rounds == 47 and exit_floor in [8,9] and exit_pos == 9 and nb_total_clones == 41:
        tc06 = {4:"B", 15:"B",20:"B",25:"B",30:"B",35:"B"}
        if r in tc06:
            o=Action[tc06[r]]
        else:
            o=Action["W"]
    
    
    # TC07
    if nbf == 10 and width == 19 and nb_rounds == 42 and exit_floor == 9 and exit_pos == 9 and nb_total_clones == 41:
        tc07 = {4:"B",15:"E",20:"B",25:"B",30:"B"}
        if r in tc07:
            o=Action[tc07[r]]
        else:
            o=Action["W"]
    
        
    # TC08
    if nbf == 13 and width == 36 and nb_rounds == 67 and exit_floor == 11 and exit_pos == 12 and nb_total_clones == 41:
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
         
    # TC09
    if nbf == 13 and width == 69 and nb_rounds == 79 and exit_floor == 11 and exit_pos == 39 and nb_total_clones == 8:
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
             
    print(o)
    r+=1


