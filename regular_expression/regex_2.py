import re
user_text = "88D88D8888"
x = re.findall("^\d{2}\D{1}\d{2}\D{1}\d{4}$", user_text)
print(x)
if x:
  print("Matches")
else:
  print("No match")