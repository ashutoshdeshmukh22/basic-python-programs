textfile = open("file.txt")
lines = textfile.readlines()
word = 0
for line in lines:
    for word in reversed(line):
        print(word, end=" ")
