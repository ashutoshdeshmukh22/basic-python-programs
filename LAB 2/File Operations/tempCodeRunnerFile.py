import os
f = open("newfile.txt", "r")
data = f.read()
lcount = sscount = scount = dcount = ccount = 0
for i in data:
    if i == "\n":
        lcount = lcount+1
    if i.isdigit():
        dcount = dcount+1
    elif i.isspace():
        scount = scount+1
    elif i.isalpha():
        ccount = ccount+len(i)
    else:
        scount = scount+1
print("Number of character:"+str(ccount))
print("Number of digit:"+str(dcount))
print("Number of space"+str(scount))
print("Number of special symbols"+str(sscount))
print("Number of line"+str(lcount+1))
print("Current file path", os.getcwd())
f.close()
