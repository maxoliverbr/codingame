import sys
import math
import re

c=[]
cc = 0
n = int(input())

data = sys.stdin.read().replace("\n",":")

lines = data
matches = re.findall(r'\((.*?)\)', lines)

for match in matches:
    sm=""
    if "|" in match:
        m = match.split("|")
        lm = len(m)
        sm=m[cc%lm]
        lines = lines.replace(match,sm,1)
        cc+=1
    else:
        sm = match
        cc+=1
    
lines = lines.replace("(","") 
lines = lines.replace(")","") 
lines = lines.replace(":","\n")
print(lines)
