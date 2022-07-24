fname = input("Enter the name of the File:")
try:
    comment = "#'''"
    with open(fname, "r",) as f:
        data = f.read()
        for i in comment:
            data = data.replace(i, "")
    with open(fname, "w",) as f1:
        f1.write(data)
except FileNotFoundError as msg:
    print(msg)
