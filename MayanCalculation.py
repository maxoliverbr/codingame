import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def d20(n):
    r = n%20
    d = []
    dr = 0
    while True:
        if n>20:
            dr = int(n/20)
            d.append(dr)
            #print(d, file=sys.stderr, flush=True)
            n = dr
        else:
            return (dr,r)
    return 0

def print_mayan_number(dict,n,l,h):
    nstr = str(n)
    d = int(n/20)
    r = n%20
    for j in range(len(nstr)):
        nn = int(nstr[j])
        #print(n,nn, file=sys.stderr, flush=True)
        for i in range(h):
            #print(n,n*l, file=sys.stderr, flush=True)
            print(dict[i][nn*l:(nn*l)+l])
        print("")

def find_mayan_number(dict, num,l,h):
    
    mayan = -1
    for j in range(0,len(dict[0]),4):
        #print(num[0], dict[0][j:j+l], file=sys.stderr, flush=True)

        if  num[0] == dict[0][j:j+l] and \
            num[1] == dict[1][j:j+l] and \
            num[2] == dict[2][j:j+l] and \
            num[3] == dict[3][j:j+l]:
            return int(j/4)
    return -1
            

numeral = []
num_1line = []
num_2line = []

l, h = [int(i) for i in input().split()]
for i in range(h):
    numeral.append(input())

#for i in range(h):
#    print(numeral[i], file=sys.stderr, flush=True)

s1 = int(input())
for i in range(s1):
    num_1line.append(input())

#for i in range(h):
#   print(num_1line[i], file=sys.stderr, flush=True)

s2 = int(input())
for i in range(s2):
    num_2line.append(input())
#for i in range(h):
#    print(num_2line[i], file=sys.stderr, flush=True)

operation = input()
n1 = find_mayan_number(numeral,num_1line,l,h)
n2 = find_mayan_number(numeral,num_2line,l,h)

#print("O ", operation, file=sys.stderr, flush=True)

r = None
if operation =="+":
    r = n1+n2
elif operation =="-":
    r = n1-n2
elif operation =='*':
    r = n1*n2
elif operation =='/':
    r = n1/n2
#print("R ",r,n1,n2, operation, file=sys.stderr, flush=True)

print_mayan_number(numeral,r,l,h)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

#print("result")
