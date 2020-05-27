import re
txt = "12okokokokaw"
x = re.findall("[ok]{6,}", txt)
print(x)
if x:
  print("Matches")
else:
  print("No match")