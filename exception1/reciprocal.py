import numpy as nm
list = [2.0,0.4,1,0,0.0]
for i in list:
    try:
        x = nm.reciprocal(i)
        print (x)
    except:
        print ("Error occurs on list")
