def hill(l):
    flag = 0
    i = 1
    while i < len(l):
        if(l[i] < l[i-1]):
            flag = 1
        i = i+1
        if (flag == 0):
            return (True)


def valley(l):
    flag = 0
    i = 1
    while i < len(l):
        if(l[i] > l[i-1]):
            flag = 1
            i = i+1
        if (flag == 0):
            return(True)


def hillvalley(l):
    if hill(l) == True:
        return(False)
    elif valley(l) == True:
        return(False)
    else:
        return(True)


print(hillvalley([3, 2, 1]))
