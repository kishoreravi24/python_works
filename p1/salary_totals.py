#Reading a file
f = open("salary.txt","r")
total = 0
getting_index =0
for x in f:
    total = total + int(filter(str.isdigit,x))
    getting_index = getting_index+1
print "Total:",total
average = total/getting_index
print "Average:",average