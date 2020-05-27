import re
txt = "1abCDe"
x = re.findall("^\d[a-zA-z]{5}$", txt)
print(x)
if x:
  print("Matches")
else:
  print("No match")