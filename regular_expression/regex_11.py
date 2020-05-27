import re
txt = "#fff"
x = re.findall("#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6})", txt)
print(x)
if x:
  print("Matches")
else:
  print("No match")