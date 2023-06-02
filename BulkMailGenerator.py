"""
7
(Hellox|Hi|Bonjour|Salut|Hey) (les amis|codersx|bande de @$%*),

I keep getting an error( 492x|) in the notification area.
Are you aware of that?

(Bye|Ciao|Fsck off|Best regardsx),
Your Name Here

Hello coders,

I keep getting an error 492 in the notification area.
Are you aware of that?

Best regards,
Your Name Here


7
(No choice)
(Empty choice|)
Lotsa (1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39|40|41|42|43|44|45|46|47|48|49|50|51|52|53|54|55|56|57|58|59|60|61|62|63|64|65|66|67|68|69|70|71|72|73|74|75|76|77|78|79|80|81|82|83|84|85|86|87|88|89|90|91|92|93|94|95|96|97|98|99|100) choices
Does it (wrap|unwrap)?
(Multi
line|Multi
line)


No choice

Lotsa 3 choices
Does it unwrap?
Multi
line
"""
import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
c=[]
cc = 0
n = int(input())

data = sys.stdin.read().replace("\n",":")

os=""
line = data
ml=[]
lines = data.split(":")

for line in lines:
    o=[]
    sm=""
    trechos = line.split(" ")
    for trecho in trechos:
        print(trecho, file=sys.stderr, flush=True)    
        if "(" in trecho and ")" in trecho:
            matches = re.findall(r'\((.*?)\)', trecho)
            #print(matches, file=sys.stderr, flush=True)    
            for match in matches:
                if "|" in match:
                    m = match.split("|")
                    lm = len(m)
                    sm = m[cc%lm]
                    o.append(sm)
                    os+=sm
                else:
                    sm = match
                    o.append(sm)
                    os+=sm
                cc+=1
        else:    
            o.append(trecho)
            os+=trecho
            
    
    #print(os, file=sys.stderr, flush=True)
    
    
    #print(cc,lm,(cc%lm),m, file=sys.stderr, flush=True)
    
    
    print(*o, file=sys.stderr, flush=True)    
os = os.replace(":","\n")
print(os)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

