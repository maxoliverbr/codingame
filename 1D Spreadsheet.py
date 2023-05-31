import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
n = int(input())
v = []

def ADD(x,y,i):
    r = int(x)+int(y)
    v[i]=(str(r),"c")
    #print("Av = ", v[i], x,y, file=sys.stderr, flush=True)
    return(r)

def SUB(x,y,i):
    r = int(x)-int(y)
    v[i]=(str(r),"c")
    #print("Sv = ", v[i], file=sys.stderr, flush=True)
    return(r)

def MULT(x,y,i):
    r = int(x)*int(y)
    v[i]=(str(r),"c")
    #print("Mv = ", v[i], file=sys.stderr, flush=True)
    return(r)

def VALUE(x,y,i):
    #print("Vv = ", v[i], file=sys.stderr, flush=True)
    v[i]=(str(x),"c")
    return x

o = []
for i in range(n):
    operation, arg_1, arg_2 = input().split()
    if operation=="VALUE":
        if arg_1=="_":
            arg_1="0"
        if arg_2=="_":
            arg_2="0"
    o.append((operation,arg_1,arg_2))

#print("-----", file=sys.stderr, flush=True)   

for i in range(n):
    if o[i][0]=="VALUE" and "$" not in o[i][1] and "$" not in o[i][2]:
        v.append((o[i][1],"c"))
    else:
        v.append(('0','nc'))

    if "$" not in o[i][1] and "$" not in o[i][2]:
        f =    o[i][0]
        arg1 = int(o[i][1].replace("$",""))
        arg2 = int(o[i][2].replace("$",""))
        r = eval(f"{f}({arg1},{arg2},{i})")

oo=[]
calc_start = False
calc_end = False
r=0

while calc_end == False:
    sk=0
    for i in range(n):
        
        f =    o[i][0]
        arg1 = o[i][1]
        arg2 = o[i][2]
        varg1= None
        varg2= None
        
        if v[i][1]=="nc":
                if "$" in arg1:
                    iarg1 = int(arg1.replace("$",""))
                    if v[iarg1][1]!="nc":
                        varg1 = int(v[iarg1][0])
                    else:
                        continue
                else:
                    varg1 = int(arg1)

                if "$" in arg2:
                    iarg2 = int(arg2.replace("$",""))
                    if v[iarg2][1]!="nc":
                        varg2 = int(v[iarg2][0])
                    else:
                        continue
                else:
                    varg2 = int(arg2)
                oo.append(eval(f"{o[i][0]}({varg1},{varg2},{i})"))    
        else:
            sk+=1      

    for i in range(n):
        if v[i][1]=="nc":
            calc_end=False
            break
        else:
            calc_end=True

for i in range(n):
    print(v[i][0])
