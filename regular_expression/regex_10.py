import re
file1 = open("string10.txt","r")
file2 = open("string10.txt","r")
count =0
word_counts = 0
lines = 0
for x in file1:
    total_count = re.findall(r"\b(Because)",x)
    word_count = re.findall(r"we",x)
    word = re.search("whimper",x)
    if word:
        start_word = word.start()
        start_end = word.end()
    replace_word = re.sub("we","you",x)
    print replace_word
    if total_count:
        count = count+1
    if word_count:
        word_counts = word_counts + 1
    lines = lines + 1
    
print "1: ",count
print "\n2: ",word_counts
print "\n3 Line: ",lines,"start:",start_word," end: ",start_end,"\n"
