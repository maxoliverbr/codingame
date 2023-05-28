import sys
nbf,w,nbr,ex,exp,nbt,nba,nbes=[int(i) for i in input().split()]
es=[]
for i in range(nbes):
 es.append([int(j) for j in input().split()])
es=sorted(es)
o,R,L,B,W="","RIGHT","LEFT","BLOCK","WAIT"
p_c_f=0
fb=False
while True:
 inputs=input().split()
 cf,cp,d=int(inputs[0]),int(inputs[1]),inputs[2]
 if nbes!=0:
  if cf==ex:ef=es[cf-1][0];ep=es[cf-1][1]
  else:ef=es[cf][0];ep=es[cf][1]
 else:
  ef=0
  ep=0
 if cp>ep and cf==ef and d==R:o=B
 elif cp<ep and cf==ef and d==L:o=B
 elif cp>ep and cf==ef and d==R:o=B
 elif cf==ex and cp>exp and d==R:o=B
 elif cf==ex and cp>exp and d==L:o=W
 elif cp==ep and p_c_f!=cf and fb==False:
  o=B
  fb=True
 elif cp<ep and cf==ef and d==R:o=W
 elif cp>ep and cf==ef and d==L:o=W
 p_c_f=cf
 print(o)
