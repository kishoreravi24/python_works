import re
string_val = "s= https:en.wikipedia.org"
index = 0
lower=[]
capital=[]
x = re.findall("wikipedia",string_val)
if x:
    for i in string_val:
        if (i>='A' and i<='Z'):
            capital.append(index)
        elif (i>='a' and i<='z'):
            lower.append(index)
        index = index + 1
print ("capital: ")
for i in capital:
    print i
print("\nlower: ")
for i in lower:
    print i