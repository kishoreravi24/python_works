import re
txt = "kites"
x = re.findall("^[a-zA-Z]+s$", txt)
print(x)
if x:
  print("Matches")
else:
  print("No match")