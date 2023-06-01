"""
7
(Hellox|Hi|Bonjour|Salut|Hey) (les amis|codersx|bande de @$%*),

I keep getting an error( 492x|) in the notification area.
Are you aware of that?

(Bye|Ciao|Fsck off|Best regardsx),
Your Name Here

Hello coders,

I keep getting an error 492 in the notification area.
Are you aware of that?

Best regards,
Your Name Here
"""
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
c=[]
cc = 0
n = int(input())
for i in range(n):
    o=[]
    os=""
    line = input()
    ll = line.replace("(",",")
    ll = ll.replace(")",",")
    ll = ll.split(",")
    print(ll, file=sys.stderr, flush=True)
    for j in ll:
        if "|" in j:
            lj=j.split("|")
            nc = len(lj)
            mcc = cc%nc
            #o.append(lj[i])
            os+=lj[mcc]
            cc+=1
            print(lj[mcc], file=sys.stderr, flush=True)
            print(i, nc, cc, file=sys.stderr, flush=True)
        else:
            #print(j, file=sys.stderr, flush=True)
            #o.append(j)
            os+=j
    print(os)
    #print(o, file=sys.stderr, flush=True)
    #print(c, file=sys.stderr, flush=True)
        
#for i in o:
#    print(i)
    

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

