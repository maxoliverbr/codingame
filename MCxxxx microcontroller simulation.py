import sys
import math
import json

"""
Line 1 : An integer K representing the length of the Input Data array
Line 2 : K integers separated by white spaces representing your Input Data
Line 3 : An integer N representing the number of lines of code
Next N lines : A Line of 

1
4
7
mov x0 dat
+ mov dat x1
- mov dat x1
teq dat 0
+ add 1
- sub 1
mov acc x1


"""

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
class CODE:
    def __init__(self, conditional, instruction, count):
        self.conditional = ""
        self.code = "" # temp storage
        self.execcount = 0 # store result arithmetric instruction
        
    def __repr__(self):
        return f"'{self.conditional}' '{self.code}' {self.execcount}"
    

class CPU:
    def __init__(self, dat, acc, x0, x1, line, labels):
        self._dat = 0 # temp storage
        self._acc = 0 # store result arithmetric instruction
        self._x0 = [] # input
        self._x1 = [] # output
        self._line = 0
        self._labels = {}
        self._cpucounter = 0
        self.teq = None
        self.tgt = None
        self.tlt = None
        self.tcp = None
    
    
    @property
    def x0(self):
        return self._x0

    @x0.setter
    def x0(self,new_x0):
        if new_x0>999:
            self._x0.append(999)
        elif new_x0<-999:
            self._x0.append(-999)
        else:
            self._x0.append(new_x0)

    @property
    def x1(self):
        return self._x1
    
    @x1.setter
    def x1(self,new_x1):
        if new_x1>999:
            self._x1.append(999)
        elif new_x1<-999:
            self._x1.append(-999)
        else:
            self._x1.append(new_x1)

    @property
    def acc(self):
        return self._acc

    @acc.setter
    def acc(self,new_acc):
        if new_acc>999:
            self._acc=999
        elif new_acc<-999:
            self._acc=-999
        else:
            self._acc=new_acc

    @property
    def dat(self):
        return self._dat

    @dat.setter
    def dat(self,new_dat):
        if new_dat>999:
            self._dat=999
        elif new_dat<-999:
            self._dat=-999
        else:
            self._dat=new_dat

    @property
    def line(self):
        return self._line

    @line.setter
    def line(self,new_line):
        self._line=new_line

    @property
    def labels(self):
        return self._labels

    @labels.setter
    def labels(self,new_label):
        self._labels=new_label

    @property
    def cpucounter(self):
        return self._cpucounter

    @cpucounter.setter
    def cpucounter(self,new_cpucounter):
        self._cpucounter=new_cpucounter


ic = []
my_cpu = CPU(0,0,[],[],0,[])


def MOV(x,y):
    #print("MOV= ",x,y,my_cpu.x0, my_cpu.x1, my_cpu.dat, my_cpu.acc, file=sys.stderr, flush=True)
    if x == "X0" and y=="X1": my_cpu.x1.append(my_cpu.x0.pop(0))
    if x == "X0" and y=="DAT": my_cpu.dat=my_cpu.x0.pop(0)
    if x == "X0" and y=="ACC": my_cpu.acc=my_cpu.x0.pop(0)
    if x == "DAT" and y=="ACC": my_cpu.acc=my_cpu.dat
    if x == "ACC" and y=="X1": my_cpu.x1.append(my_cpu.acc)
    if x.isnumeric() and y=="ACC": my_cpu.acc = int(x)
    if x.isnumeric() and y=="X1": my_cpu.x1.append(int(x))
    #print(my_cpu.x0, my_cpu.x1, my_cpu.dat, my_cpu.acc, file=sys.stderr, flush=True)
    pass

def JMP(x):
    x=x+":"
    if x in my_cpu.labels:
        my_cpu.line = my_cpu.labels[x]
    pass

def ADD(x):
    if x == "DAT": my_cpu.acc = my_cpu.dat+my_cpu.acc
    if x.isnumeric():
        my_cpu.acc=my_cpu.acc+int(x)
    pass

def SUB(x):
    #print("SUB= ", x, my_cpu.x0, my_cpu.x1, my_cpu.dat, my_cpu.acc, file=sys.stderr, flush=True)
    if x == "DAT": my_cpu.acc = my_cpu.acc-my_cpu.dat
    elif x.isnumeric():
        my_cpu.acc = my_cpu.acc-int(x)
    pass

def MUL(x):
    if x == "DAT": my_cpu.acc = my_cpu.acc*my_cpu.dat
    if x.isnumeric():
        my_cpu.acc = my_cpu.acc*int(x)
    pass

def NOT():
    if my_cpu.acc == 0:
        my_cpu.acc = 100
    else:
        my_cpu.acc = 0


def DGT(x):
    if x.isnumeric():
        if int(x)==2 and my_cpu.acc<=99:
            my_cpu.acc=0
        else:
            my_cpu.acc = int(str(my_cpu.acc)[len(str(my_cpu.acc))-int(x)-1])
    pass


def DST(x,y):
    #print(f"DST= {x} {y} {my_cpu.acc:08}", file=sys.stderr, flush=True)
    mycpuaccstr = f"{my_cpu.acc:08}"
    if   x.isnumeric() and y.isnumeric():  
        mycpuaccstr = mycpuaccstr[:int(x)] + chr(y) + mycpuaccstr[int(x)+1:]
        my_cpu.acc = int(mycpuaccstr[::-1])
    elif x.isnumeric() and y=="DAT":
        mycpuaccstr = mycpuaccstr[:int(x)] + str(my_cpu.dat) + mycpuaccstr[int(x)+1:]
        my_cpu.acc = int(mycpuaccstr[::-1])
    #print(f"DST= {x} {y} {my_cpu.acc:08} {mycpuaccstr}", file=sys.stderr, flush=True)
    pass


"""

1
4
7
mov x0 dat
+ mov dat x1
- mov dat x1
teq dat 0
+ add 1
- sub 1
mov acc x1

out:
-1

mov x0 dat->dat=4
teq dat 0->False
sub 1->acc-1=-1
mov acc x1->x1=-1

"""

def TEQ(x,y):
    if x=="DAT" and y.isnumeric():
        if my_cpu.dat == int(y):
            my_cpu.teq = True
        else:
            my_cpu.teq = False
    print("TEQ= ", x, y, my_cpu.teq, file=sys.stderr, flush=True)

    pass



"""
1
0
7
mov x0 dat
tgt dat -1
+ mov 1 x1
- mov -1 x1
tlt dat 1
+ mov 1 x1
- mov -1 x1

mov x0 dat-> dat = 0
tgt dat -1-> True
mov -1 x1-> x1= 1
tlt dat 1-> True
mov 1 x1 -> x1 = 1 1

"""
def TGT(x,y):
    if x=="DAT" and y.isnumeric():
        if my_cpu.dat>int(y):
            my_cpu.tgt = True
        else:
            my_cpu.tgt = False
    print("TGT= ", x, y, my_cpu.tgt, file=sys.stderr, flush=True)            
    pass

def TLT(x,y):
    if x=="DAT" and y.isnumeric():
        if my_cpu.dat<int(y):
            my_cpu.tlt=True
        else:
            my_cpu.tlt=False
    print("TLT= ", x, y, my_cpu.tlt, file=sys.stderr, flush=True)                        
    pass


"""
1
0
10
mov x0 dat
tcp dat -1
+ mov 1 x1
- mov -1 x1
tcp dat 0
+ mov 1 x1
- mov -1 x1
tcp dat 1
+ mov 1 x1
- mov -1 x1
"""

def TCP(x,y):
    pass

k = int(input())
for i in input().split():
    my_cpu.x0.append(int(i))

n = int(input())

for i in range(n):
    line_code = CODE("","",0)
    instruction = input().upper()
    ins = instruction.split()
    print("INS= ", ins[0], file=sys.stderr, flush=True)
    if ":" in ins[0]:
        my_cpu.labels[ins[0]]=i  
        instruction = instruction.replace(ins[0],"").strip()
        #print(f"LABEL= '{instruction}'", file=sys.stderr, flush=True)
        if instruction=="":
            instruction="#"
        line_code.conditional = ""
        line_code.code = instruction
        line_code.execcount = 0
    elif "+" in ins[0] or "-" in ins[0]:
        line_code.conditional = ins[0]
        line_code.code = instruction[2:]
        line_code.execcount = 0
    else:
        line_code.conditional = ""
        line_code.code = instruction
        line_code.execcount = 0
    ic.append(line_code)
    
        

print("IC= ", ic, file=sys.stderr, flush=True)

while(my_cpu.line<n):
    #for ins in ic:
        print(f"CPU X0={my_cpu.x0} X1={my_cpu.x1} DAT='{my_cpu.dat}' ACC='{my_cpu.acc}'", file=sys.stderr, flush=True)
        ins = ic[my_cpu.line]
        my_cpu.cpucounter+=1
        #jsonStr = json.dumps(my_cpu.__dict__)
        #print(jsonStr, file=sys.stderr, flush=True)
        #jsonStr = json.dumps(ins.__dict__)
        #print(jsonStr, file=sys.stderr, flush=True)

        if my_cpu.teq == True and ins.conditional=="-":
            my_cpu.line+=1
            continue
        elif my_cpu.teq == False and ins.conditional=="+":
            my_cpu.line+=1
            continue
        elif my_cpu.tgt == True and ins.conditional=="-":
            my_cpu.line+=1
            continue
        elif my_cpu.tgt == False and ins.conditional=="+":
            my_cpu.line+=1
            continue
        else:
            i = ins.code.split()
            if i[0] == "#":
                pass
            elif i[0] == "@":
                #print("@ jmp calc",ins, file=sys.stderr, flush=True)
                if ins.execcount == 1:
                    print("@ NO EXEC ",ins, file=sys.stderr, flush=True)
                    pass
                else:
                    ins.execcount = 1
                    r = eval(f"{i[1]}('{i[2]}')")
                    continue
            elif ":" in i[0]:
                pass
            elif i[0] == "JMP":
                r = eval(f"{i[0]}('{i[1]}')")
                continue
            elif i[0] == "MOV":
                r = eval(f"{i[0]}('{i[1]}','{i[2]}')")
            elif i[0] =="ADD" or i[0] == "SUB" or i[0]=="MUL":
                r = eval(f"{i[0]}('{i[1]}')")
            elif i[0] =="NOT":
                r = eval(f"{i[0]}()")
            elif i[0] =="DGT":
                r = eval(f"{i[0]}('{i[1]}')")
            elif i[0] =="DST":
                r = eval(f"{i[0]}('{i[1]}','{i[2]}')")
            elif i[0] =="TEQ":
                r = eval(f"{i[0]}('{i[1]}','{i[2]}')")
            elif i[0] =="TGT":
                r = eval(f"{i[0]}('{i[1]}','{i[2]}')")
            elif i[0] =="TLT":
                r = eval(f"{i[0]}('{i[1]}','{i[2]}')")

            my_cpu.line+=1

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(*my_cpu.x1)
