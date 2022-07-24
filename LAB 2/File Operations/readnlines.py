file = "newfile.txt"
number = int(input("Enter number of n: "))
with open("newfile.txt") as f:
    print("First lines")
    for line2 in (f.readlines()[:number]):
        print(line2)
    print("\n")
    with open("newfile.txt") as f:
        print("Last lines")
        for line1 in (f.readlines()[-number:]):
            print(line1)
