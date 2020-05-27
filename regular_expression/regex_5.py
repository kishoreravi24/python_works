import re
string_val = "Betty bought some butter. The butter was bitter"
ans = re.findall("butter",string_val)
index = 0
for i in ans:
    index = index + 1
print index