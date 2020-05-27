import re
txt = "12avVA"
x = re.findall("^\d{2,}[a-z]*[A-Z]*$", txt)
print(x)
if x:
  print("Matches")
else:
  print("No match")