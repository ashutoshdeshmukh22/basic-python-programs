
def removeDuplicates(s):
    l = s.split()
    k = []
    for i in l:
        # If condition is used to store unique string
        # in another list 'k'
        if (s.count(i) >= 1 and (i not in k)):
            k.append(i)
    print(' '.join(k))


removeDuplicates('My name is Ashu and my name')

# OR

# string = 'My name is Ashu and my name'
# print(' '.join(dict.fromkeys(string.split())))
