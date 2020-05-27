import re
example_text = '88D88D888888D88D888888D88D888888D88D8888795 1'
user_text=raw_input("Enter A text: ")
x = re.findall("[a-zA-Z02468]{40}[13579\s]{5}", user_text)
print(x)
if x:
  print("Matches")
else:
  print("No match")