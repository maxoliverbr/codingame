import sys
import math

# Save humans, destroy zombies!


def dist(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

# game loop
while True:
    humans = []
    zombies =[]
    dh=[]
    dz=[]
    dhz=[]

    x, y = [int(i) for i in input().split()]
    human_count = int(input())
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        humans.append((human_id, human_x, human_y))
        dh.append((i,dist(x,y,human_x,human_y)))
    
    dh.sort(key=lambda x:x[1])
    
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        zombies.append((zombie_id, zombie_x, zombie_y))
        dz.append((i,dist(x,y,zombie_x,zombie_y)))
    
    dz.sort(key=lambda x:x[1])    
    
    for i in range(zombie_count):
        dhz.append((i,dist(humans[dh[0][0]][1],humans[dh[0][0]][2],zombies[i][1],zombies[i][2])))

        
    dhz.sort(key=lambda x:x[1])   
    print(f"{dhz[0]} {dh[0]} {dz[0]}", file=sys.stderr, flush=True)
    print(f"{zombie_count}", file=sys.stderr, flush=True)

    if dh[0][1]<2000 and dz[0][1]>100:
        print(f"{zombies[dz[0][0]][1]} {zombies[dz[0][0]][2]}")
    elif human_count==3 and zombie_count<12:
        print(f"{zombies[dz[0][0]][1]} {zombies[dz[0][0]][2]}")
    elif human_count==4:
        print(f"{humans[dh[0][0]][1]} {humans[dh[0][0]][2]}")      
    elif human_count>3:
        print(f"{humans[dh[0][0]][1]} {humans[dh[0][0]][2]}")
    elif dz[0][1]<dh[0][1] and human_count>3:
        print(f"{zombies[dz[0][0]][1]} {zombies[dz[0][0]][2]}")
    elif human_count == zombie_count and human_count>1:
        print(f"{humans[dh[1][0]][1]} {humans[dh[1][0]][2]}")   
    elif zombie_count<2:
        print(f"{zombies[dz[0][0]][1]} {zombies[dz[0][0]][2]}")     
    else:
        print(f"{humans[dh[0][0]][1]} {humans[dh[0][0]][2]}")        
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    #print(f"{humans[dh[0][0]][1]} {humans[dh[0][0]][2]}", file=sys.stderr, flush=True)
