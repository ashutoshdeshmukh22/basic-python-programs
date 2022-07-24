
import os
import threading


def copy():
    with open('India.txt', 'r') as firstfile, open('Hello.txt', 'a') as secondfile:
        # read content from first file
        for line in firstfile:
            # append content to second file
            secondfile.write(line)


def count():
    f = open('India.txt', 'r')
    data = f.read()
    lcount = sscount = scount = dcount = ccount = 0
    for i in data:
        if i == '\n':
            lcount = lcount+1
        if i.isdigit():
            dcount = dcount+1
        elif i.isspace():
            scount = scount+1
        elif i.isalpha():
            ccount = ccount+len(i)
        else:
            scount = scount+1

    print("Number of character: "+str(ccount))
    print("Number of digit:"+str(dcount))
    print("Number of space" + str(scount))
    print("Number of special symbols" + str(sscount))
    print("Number of line"+str(lcount+1))
    print("Current file path", os.getcwd())
    f.close()


t1 = threading.Thread(target=copy)
t2 = threading.Thread(target=count)

t1.start()
t2.start()
t1.join()
t2.join()
