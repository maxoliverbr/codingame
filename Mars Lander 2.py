import sys
import math

# Save the Planet.
# Use less Fossil Fuel.

MAX_ANGLE = 45

def dist(x1,y1,x0,y0):
    return math.sqrt((x1-x0)**2+(y1-y0)**2)

def calculate_vectordy(angle,dy, distance):
    r = angle
    try:
        r = math.acos(dy/distance)
    except:
        print("EX",angle, dy, distance, file=sys.stderr, flush=True)
        return r
    return r

def calculate_vectordx(dx, distance):
    r = 0
    try:
        r = math.asin(dx/distance)
    except:
        print("EX",angle, dx, distance, file=sys.stderr, flush=True)
        return r
    return r

def stable(hs,vs):
    if hs in range(-2,2) and vs in range(-2,2):
        return True
    else:
        return False

n = int(input())  # the number of points used to draw the surface of Mars.
flat_x0, flat_x1, flat_y = 0,0,0
land = []
angle = ""
angle_pos = ""

for i in range(n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    land.append((land_x,land_y))

#print(land, file=sys.stderr, flush=True)

for i in range(n-1):
    #print(land[i][0],land[i][1], file=sys.stderr, flush=True)
    if land[i][1]==land[i+1][1]:
        flat_x0 = land[i][0]
        flat_x1 = land[i+1][0]
        flat_y  = land[i][1]
        break


xland_optimal = int((flat_x1+flat_x0)/2)

stable_check = False
landing_ok = False
high_ground = False
trust = 0
t = 0
# game loop
while True:
    # hs: the horizontal speed (in m/s), can be negative.
    # vs: the vertical speed (in m/s), can be negative.
    # f: the quantity of remaining fuel in liters.
    # r: the rotation angle in degrees (-90 to 90).
    # p: the thrust power (0 to 4).
    x, y, hs, vs, f, r, p = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    #print(xland_optimal, file=sys.stderr, flush=True)
    
    distance_x0 = dist(x,y,flat_x0, flat_y)
    dx0 = flat_x0-x
    
    distance_x1 = dist(x,y,flat_x1, flat_y)
    dx1 = flat_x1-x
    
    landing_zone = False

    dy = y-flat_y

    angle_vector_x0 = calculate_vectordx(dx0,distance_x0)
    angle_vector_x1 = calculate_vectordx(dx1,distance_x1)
   
    if dx0 < dx1:
        angle_vector = angle_vector_x0
    else:
        angle_vector = angle_vector_x1

    angle = -angle_vector*90+hs

    #print("ZZ",stable(hs,vs),dy,distance_x0,dx0,angle_vector_x0,distance_x1,dx1,angle_vector_x1, file=sys.stderr, flush=True)    
    
    if stable_check is False and t>0:
        stable_check = stable(hs,vs)
        print("CKSTABLE",stable_check, file=sys.stderr, flush=True)

    if stable_check is not True:
        print("NOTSTABLE",x, file=sys.stderr, flush=True)
        if trust == 3:
            trust = 4
        else:
            trust = 3
        if vs<-40:
            trust = 4

        if x>flat_x0 and x<flat_x1:
            landing_zone = True
            if vs<-20:
                trust =4
                

    if stable_check == True:
        print("STABLE",x,y, flat_y, file=sys.stderr, flush=True)
        angle = 0
        trust = 2
        if vs < -30:
            trust = 4
        if vs >0:
            trust = 3


    if landing_zone == True and stable_check == True:
        angle = 0
    
    if landing_zone == True and hs == 0 or landing_ok == True:
        angle = 0
        if vs < -20:
            trust = 4
        if vs >0:
            trust = 3
        landing_ok = True
        print("LANDOK",angle, trust, file=sys.stderr, flush=True)

    #Critical stage landing
    if dy < 500 and dy > -250 and landing_ok == False and high_ground == False:
        
        angle = 0
        trust = 4
        if hs<0 and vs<0 and landing_ok == False:
            angle = 10-int(-hs/2)
        elif hs>0 and vs<0 and landing_ok == False:
            angle =-10-int(-hs/2)
        stable_check = False
        print("B500",angle, flat_y, file=sys.stderr, flush=True)

        
    if dy < 200 and landing_zone == True:
        angle = 0
        
        if vs < -30:
            trust = 4
        else:
            trust = 2
        print("CRITICAL",x,y, trust, file=sys.stderr, flush=True)

    if dy<0 or high_ground == True:
        print("HG",x,y,dy,flat_y, file=sys.stderr, flush=True)
        if high_ground == False:
            high_ground = True
        if hs<-10:
            angle=-10
        else:
            angle = 20
        if vs>10:
            trust = 3
        else:
            trust = 4

    if high_ground == True and vs>20:
        print("HGVS",x,y,dy,flat_y, file=sys.stderr, flush=True)
        trust = 3
        angle = 10
        if hs<-40:
            angle = int(angle/2)

    if high_ground == True and landing_zone == True:
        print("HGLZ",x,y,dy,flat_y, file=sys.stderr, flush=True)

        if hs<-5:
            angle = hs
        else:
            angle = 0
        
        if vs>-20:
            trust = 2
        else:
            trust = 4
        
    if angle > MAX_ANGLE:
        angle = MAX_ANGLE
    elif angle < -MAX_ANGLE:
        angle = -MAX_ANGLE

    print(str(int(angle)),str(trust))
    t += 1
