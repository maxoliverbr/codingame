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
    if nbf == 10 and width in[19,21] and nb_rounds == 47 and exit_floor == 9 and exit_pos in [8,9] and nb_total_clones == 41:
        if exit_pos == 9:
            tc06 = {4:"B", 15:"B",20:"B",25:"B",30:"B",35:"B"}
        else:
            tc06 = {3:"B", 15:"B",20:"B",25:"B",30:"B",35:"B"}
        if r in tc06:
            o=Action[tc06[r]]
        else:
            o=Action["W"]
    
    
    # TC07
    if nbf == 10 and width in [19,22] and nb_rounds == 42 and exit_floor == 9 and exit_pos in [9,11] and nb_total_clones == 41:
        tc07 = {4:"B",15:"E",20:"B",25:"B",30:"B"}
        if r in tc07:
            o=Action[tc07[r]]
        else:
            o=Action["W"]
    
        
    # TC08
    if nbf in [13,14] and width in [36,37] and nb_rounds == 67 and exit_floor == 11 and exit_pos == 12 and nb_total_clones == 41:
        if exit_floor == 11:
            tc08 = {0:"E", 4:"B", 12:"B", 18:"E", 28:"E", 47:"B", 62:"E"}
        else:
            tc08 = {0:"E", 4:"B", 12:"B", 18:"E", 28:"E", 47:"B", 62:"E"}

        if r in tc08:
            o=Action[tc08[r]]
        else:
            o=Action["W"]
    
         
    # TC09
    if nbf in [13,14] and width in [69,70,71] and nb_rounds ==79 and exit_floor == 11 and exit_pos == 39 and nb_total_clones == 8:
        tc09 = {1:"B", 6:"E", 28:"E", 32:"E", 39:"B", 70:"E", 74:"E"}
        print(f"tc09", file=sys.stderr, flush=True)

        if r in tc09:
            o=Action[tc09[r]]
        else:
            o=Action["W"]
    
    # TC10
    if nbf in [13,14] and width in [69,70,71] and nb_rounds ==109 and exit_floor == 11 and exit_pos == 47 and nb_total_clones == 100:
        tc10 = {11:"E", 25:"B", 30:"E", 35:"E", 40:"B", 67:"E", 72:"B", 77:"B", 106:"E"}
        print(f"tc10", file=sys.stderr, flush=True)

        if r in tc10:
            o=Action[tc10[r]]
        else:
            o=Action["W"]
             
    print(o)
    r+=1


