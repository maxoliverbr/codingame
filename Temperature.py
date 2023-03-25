t=[]
n=int(input())
if n==0:
    print(0)
elif n==1:
    print(input())
else:
    for i in input().split():
        t.append(int(i))  
    t.sort(key=lambda a: abs(a))
    if t[0] < 0 and t[1] < 0:
        print(t[0])
    elif abs(t[0]) == t[1]:
        print(t[1])
    else:
        print(t[0])
