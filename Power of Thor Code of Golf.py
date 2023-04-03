a,b,c,d=map(int,input().split())
x,y=a-c,b-d
while True:
 r=int(input())
 t=s=""
 if x>0:t,x="E",x-1
 elif x<0:t,x="W",x+1
 if y>0:s,y="S",y-1
 elif y<0:s,y="N",y+1
 print(s+t)
