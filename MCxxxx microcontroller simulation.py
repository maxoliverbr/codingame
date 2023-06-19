import sys
import math
import json
import re


def is_number(s):
    return bool(re.match(r'^-?\d+(?:\.\d+)?$', s))

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

"""
1
4
7
mov x0 dat - dat = 4
+ mov dat x1
- mov dat x1
teq dat 0
+ add 1
- sub 1
mov acc x1


"""


def MOV(x,y):
    if x == "X0" and y=="X1": my_cpu.x1.append(my_cpu.x0.pop(0))
    if x == "X0" and y=="DAT": my_cpu.dat=my_cpu.x0.pop(0)
    if x == "X0" and y=="ACC": my_cpu.acc=my_cpu.x0.pop(0)

    if x == "DAT" and y=="ACC": my_cpu.acc=my_cpu.dat
    if x == "ACC" and y=="DAT": my_cpu.dat=my_cpu.acc
    
    if x == "ACC" and y=="X1": my_cpu.x1.append(my_cpu.acc)
    if x == "DAT" and y=="X1": my_cpu.x1.append(my_cpu.dat)
    
    if is_number(x) and y=="DAT": my_cpu.dat = int(x)
    if is_number(x) and y=="ACC": my_cpu.acc = int(x)
    if is_number(x) and y=="X1": my_cpu.x1.append(int(x))
    

def JMP(x):
    x=x+":"
    if x in my_cpu.labels:
        my_cpu.line = my_cpu.labels[x]
    

def ADD(x):
    if x == "DAT": my_cpu.acc = my_cpu.dat+my_cpu.acc
    if is_number(x):
        my_cpu.acc=my_cpu.acc+int(x)
    

def SUB(x):
    if x == "DAT": my_cpu.acc = my_cpu.acc-my_cpu.dat
    elif is_number(x):
        my_cpu.acc = my_cpu.acc-int(x)


def MUL(x):
    if x == "DAT": my_cpu.acc = my_cpu.acc*my_cpu.dat
    if is_number(x):
        my_cpu.acc = my_cpu.acc*int(x)
    

def NOT():
    if my_cpu.acc == 0:
        my_cpu.acc = 100
    else:
        my_cpu.acc = 0


def DGT(x):
    if is_number(x):
        if int(x)==2 and my_cpu.acc<=99:
            my_cpu.acc=0
        else:
            my_cpu.acc = int(str(my_cpu.acc)[len(str(my_cpu.acc))-int(x)-1])

"""
3
0 9 0
9
mov x0 acc
mov x0 dat
dst acc dat
dst 1 dat
dst 2 dat
mov acc x1
mov x0 acc
dst 2 dat
mov acc x1
"""

def DST(x,y):
    
    """
     | acc | Instruction | acc' |
     | 596 |  dst 0 7    | 597  |
     | 596 |  dst 1 7    | 576  |
     | 596 |  dst 2 7    | 796  |
     dst 1 1
     dst 1 dat
     dst dat 1
     dst acc 1
     dst 1 acc
     dst x0 dat
     dst x0 acc
     dst x0 1
     dst 1 x0
    """

    mycpuaccstr = f"{my_cpu.acc:08}"
    if  is_number(x) and is_number(y):  
        mycpuaccstr = mycpuaccstr[:int(x)] + str(y) + mycpuaccstr[int(x)+1:]
    elif is_number(x) and y=="DAT":
        mycpuaccstr = mycpuaccstr[:int(x)] + str(my_cpu.dat) + mycpuaccstr[int(x)+1:]
    elif x=="DAT" and is_number(y):
        mycpuaccstr = mycpuaccstr[:int(my_cpu.dat)] + str(y) + mycpuaccstr[int(my_cpu.dat)+1:]
    elif is_number(x) and y=="ACC":
        mycpuaccstr = mycpuaccstr[:int(x)] + str(my_cpu.acc) + mycpuaccstr[int(x)+1:]
    elif x=="ACC" and is_number(y):
        mycpuaccstr = mycpuaccstr[:int(my_cpu.acc)] + str(y) + mycpuaccstr[int(my_cpu.acc)+1:]
        
    my_cpu.acc = int(mycpuaccstr[::-1])

def TEQ(x,y):
    if x=="DAT" and is_number(y):
        if my_cpu.dat == int(y):
            my_cpu.teq = True
        else:
            my_cpu.teq = False
    elif x=="ACC" and is_number(y):
        if my_cpu.acc == int(y):
            my_cpu.teq = True
        else:
            my_cpu.teq = False

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
"""

def TGT(x,y):
    if is_number(x) and is_number(y):
        if int(x)>int(y):
            my_cpu.tgt = True
        else:
            my_cpu.tgt = False
    elif x=="DAT" and is_number(y):
        if my_cpu.dat>int(y):
            my_cpu.tgt = True
        else:
            my_cpu.tgt = False    
    elif x=="ACC" and is_number(y):
        if my_cpu.acc>int(y):
            my_cpu.tgt = True
        else:
            my_cpu.tgt = False    

def TLT(x,y):
    if is_number(x) and is_number(y):
        if int(x)<int(y):
            my_cpu.tlt = True
        else:
            my_cpu.tlt = False
    elif x=="DAT" and is_number(y):
        if my_cpu.dat<int(y):
            my_cpu.tlt=True
        else:
            my_cpu.tlt=False
    elif x == "ACC" and is_number(y):
        if my_cpu.acc<int(y):
            my_cpu.tlt=True
        else:
            my_cpu.tlt=False
    print("TLT= ", x, my_cpu.acc, y,  my_cpu.tlt, file=sys.stderr, flush=True)                        

def TCP(x,y):
    if x == "DAT" and is_number(y):
        if (my_cpu.dat>int(y))==True:
            print(f"TCP01 '1'", file=sys.stderr, flush=True)                        
            my_cpu.tcp=1 # +enbaled -disabled
        elif my_cpu.dat==int(y):
            print(f"TCP0= '0'", file=sys.stderr, flush=True)                        
            my_cpu.tcp=0 # +disbled -disabled
        elif my_cpu.dat<int(y):
            print(f"TCP-1= '-1'", file=sys.stderr, flush=True)                        
            my_cpu.tcp=-1 # +disabled -enabled

k = int(input())
for i in input().split():
    my_cpu.x0.append(int(i))

n = int(input())

for i in range(n):
    line_code = CODE("","",0)
    instruction = input().upper()
    ins = instruction.split()
    if ":" in ins[0]:
        my_cpu.labels[ins[0]]=i  
        instruction = instruction.replace(ins[0],"").strip()
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
    

while(my_cpu.line<n):
        #print(f"CPU X0={my_cpu.x0} X1={my_cpu.x1} DAT='{my_cpu.dat}' ACC='{my_cpu.acc}'", file=sys.stderr, flush=True)
        ins = ic[my_cpu.line]
        #print(f"INS={ins.conditional} {ins.code}", file=sys.stderr, flush=True)
        my_cpu.cpucounter+=1
        #jsonStr = json.dumps(my_cpu.__dict__)
        #print(jsonStr, file=sys.stderr, flush=True)
        #jsonStr = json.dumps(ins.__dict__)
        #print(jsonStr, file=sys.stderr, flush=True)
        
        print(f"TEQ={my_cpu.teq} {ins.conditional} {ins.code}", file=sys.stderr, flush=True)
        
        if (my_cpu.teq == None and my_cpu.tgt == None and my_cpu.tlt == None and my_cpu.tcp == None) and (ins.conditional == "+" or ins.conditional == "-"):
            my_cpu.line+=1
            continue

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
        elif my_cpu.tlt == True and ins.conditional=="-":
            my_cpu.line+=1
            continue
        elif my_cpu.tlt == False and ins.conditional=="+":
            my_cpu.line+=1
            continue
        elif my_cpu.tcp == 1 and ins.conditional=="-":
            my_cpu.line+=1
            continue
        elif my_cpu.tcp == -1 and ins.conditional=="+":
            my_cpu.line+=1
            continue
        elif my_cpu.tcp == 0 and (ins.conditional=="+" or ins.conditional=="-"):
            my_cpu.line+=1
            continue
        else:
            i = ins.code.split()
            print(f"i={i[0]} {ins.code}", file=sys.stderr, flush=True)
            if i[0] == "@":
                if ins.execcount == 1:
                    print("@ NO EXEC ",ins, file=sys.stderr, flush=True)
                else:
                    ins.execcount = 1
                    r = eval(f"{i[1]}('{i[2]}')")
                    continue
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
            elif i[0] =="TCP":
                r = eval(f"{i[0]}('{i[1]}','{i[2]}')")
            my_cpu.line+=1

print(*my_cpu.x1)
