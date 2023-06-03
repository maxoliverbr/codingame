import sys
import math


s = {"_": 0,
     "-": 1}

signals =[]
operations = []


def get_key(val):
    for key, value in s.items():
        if val == value:
            return key


def AND(x, y):
    return s[x] & s[y]


def OR(x, y):
    return s[x] | s[y]


def XOR(x, y):
    return s[x] ^ s[y]


def NAND(x, y):
    return not AND(x, y)


def NOR(x, y):
    return not OR(x, y)


def NXOR(x, y):
    return not XOR(x, y)

def get_signal(name)-> str:
    for i in signals:
        if i[0] == name:
            return i[1]
    return "None"



n = int(input())
m = int(input())

for i in range(n):
    input_name, input_signal = input().split()
    signals.append((input_name, input_signal))

#print(signals, file=sys.stderr, flush=True)

for i in range(m):
    output_name, _type, input_name_1, input_name_2 = input().split()
    operations.append((output_name, _type, input_name_1, input_name_2))

#print(operations, file=sys.stderr, flush=True)

for i in range(m):
    output_signal_name = operations[i][0]
    output_signal_op   = operations[i][1]
    input_signal_name1 = operations[i][2]
    input_signal_name2 = operations[i][3]

    signal1 = get_signal(input_signal_name1)
    signal2 = get_signal(input_signal_name2)
    
    os = ""

    for i in range(len(signal1)):
        os += get_key(eval(f"{output_signal_op}('{signal1[i]}','{signal2[i]}')"))
    #print(f"{output_signal_op}('{signal1[i]}','{signal2[i]}')", os, file=sys.stderr, flush=True)    
    print(output_signal_name, os)            
