import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
n = int(input())
v = []

def ADD(x,y,i):
    r = int(x)+int(y)
    v[i]=(str(r),"c")
    print("Av = ", v[i], x,y, file=sys.stderr, flush=True)
    return(r)

def SUB(x,y,i):
    r = int(x)-int(y)
    v[i]=(str(r),"c")
    print("Sv = ", v[i], file=sys.stderr, flush=True)
    return(r)

def MULT(x,y,i):
    r = int(x)*int(y)
    v[i]=(str(r),"c")
    print("Mv = ", v, file=sys.stderr, flush=True)
    return(r)

def VALUE(x,y,i):
    print("Vv = ", v, file=sys.stderr, flush=True)
    v[i]=(str(x),"0")
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

#print(n, file=sys.stderr, flush=True)
#print("o = ", o, file=sys.stderr, flush=True)

print("-----", file=sys.stderr, flush=True)   
for i in range(n):
    #print("Peval= ",f"{o[i][0]}({o[i][1]},{o[i][2]},{i})", file=sys.stderr, flush=True)    
    if o[i][0]=="VALUE" and "$" not in o[i][1] and "$" not in o[i][2]:
        print("PV= ",f"{o[i][0]}({o[i][1]},{o[i][2]},{i})", file=sys.stderr, flush=True)    
        v.append((o[i][1],o[i][2]))
    else:
        v.append(('0','nc'))
    if "$" not in o[i][1] and "$" not in o[i][2]:
        
        f =    o[i][0]
        arg1 = int(o[i][1].replace("$",""))
        arg2 = int(o[i][2].replace("$",""))
        
        print("eval=  ",f"{f}({arg1},{arg2},{i})", file=sys.stderr, flush=True)    
        r = eval(f"{f}({arg1},{arg2},{i})")

#print("v = ", v, file=sys.stderr, flush=True)

oo=[]
calc_start = False
calc_end = False
r=0
print("-----", file=sys.stderr, flush=True)   
while calc_end == False:
    for i in range(n):
        print("i", file=sys.stderr, flush=True)   

        
        f =    o[i][0]
        arg1 = o[i][1]
        arg2 = o[i][2]
        varg1= None
        varg2= None
        #print("V-",v, file=sys.stderr, flush=True)        
        print("X-",f"{o[i][0]}({arg1},{arg2},{i})", file=sys.stderr, flush=True)        
        
        if f!="VALUE":
            if "$" in arg1:
                iarg1 = int(arg1.replace("$",""))
                if v[iarg1][1]!="nc":
                    print("V1-",v[iarg1][0], file=sys.stderr, flush=True)        
                    print("V-",v, file=sys.stderr, flush=True)        
                    
                    varg1 = int(v[iarg1][0])
                else:
                    print("c1", file=sys.stderr, flush=True)   
                    continue
            else:
                varg1 = int(arg1)

            if "$" in arg2:
                iarg2 = int(arg2.replace("$",""))
                if v[iarg2][1]!="nc":
                    print("V1-",v[iarg2][0], file=sys.stderr, flush=True)        
                    varg2 = int(v[iarg2][0])
                else:
                    print("c2", file=sys.stderr, flush=True)   
                    continue
            else:
                varg2 = int(arg2)

            print("X-",f"{f}({varg1},{varg2},{i})", file=sys.stderr, flush=True)        
            oo.append(eval(f"{o[i][0]}({varg1},{varg2},{i})"))    
                    
            #print("ev ", i,f,arg1,arg2, file=sys.stderr, flush=True)
            #print("eval= ",f"{o[i][0]}({arg1},{arg2},{i})", file=sys.stderr, flush=True)
            #print(eval(f"{o[i][0]}({arg1},{arg2},{i})"))
            #oo.append(eval(f"{o[i][0]}({arg1},{arg2},{i})"))

    #print(oo, i,f,arg1,arg2, file=sys.stderr, flush=True)

    for i in range(n):
        if v[i][1]=="nc":
            calc_end=False
            break
        else:
            calc_end=True

    
    #if r>3:
    #    break
    #r+=1
                
        #print(f,arg1,arg2, file=sys.stderr, flush=True)
        #print("v = ", v, file=sys.stderr, flush=True)
        # Write an answer using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)

        

for i in range(n):
    print(v[i][0])
