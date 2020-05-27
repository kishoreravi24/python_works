import os.path
import random
user_text = raw_input("Filename: ")
out_arr = []
lines = []
if os.path.exists(user_text):
    print ("File already exists")
else:
    f = open(user_text,"w+")
    for i in range(1,101):
        lines.append(i)
    random.shuffle(lines)
    for i in lines:
        f.write("%i " % i)
    with open(user_text) as f:
        data = f.read()
    output = ''
    for i in data:
        if i.isdigit() == True:
            output +=i 
        else:
            out_arr.append(int(output))
            output=''
    out_arr.sort()
    for i in out_arr:
        print (i)    