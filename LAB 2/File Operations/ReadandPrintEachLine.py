L = ["Ashutosh\n", "Swanand\n", "Mayur\n"]
# Writing to file
with open("newfile.txt", "w") as fp:
    fp.writelines(L)
# Using for loop
count = 0
print("\nUsing for loop")
with open("newfile.txt") as fp:
    for line in fp:
        count += 1
        print("Line{}: {}".format(count, line.strip()))
