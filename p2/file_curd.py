user_text = raw_input("Filename: ")
f = open(user_text,"w")
old_string = raw_input("old_String: ")
with open(user_text,"w") as f:
    f.write(old_string)
new_string = raw_input("new_string: ")
with open(user_text,"w") as f:
    f.write(new_string)