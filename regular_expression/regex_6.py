import re
char = "Betty bought some butter. The butter was bitter"
x = re.findall(r"\b[bB]",char)
val = char.split()
count =0
all_count =0
for i in val:
    for j in x:
        if(i[0]==j):
            print i
            break
            

