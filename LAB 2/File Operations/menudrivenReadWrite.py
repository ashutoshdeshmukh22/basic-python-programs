import csv
flag = 0
while(True):
    print("Press 1 to write a file")
    print("Press 2 to read a file")
    print("Press 3 to exit")
    n = int(input("Enter your choice:"))
    if(n == 1):
        with open('marks.csv', "a", newline='') as f1:
            w = csv.writer(f1)
            if flag == 0:
                w.writerow(["Roll", "Name", "Unit1", "Unit2", "Unit3", "Unit4", "Unit5",
                           "Assignment1", "Assignment2", "Midterm", "Perlim", "Total"])
                flag = 1
                nn = int(input("Enter Number of record to be inserted:"))
                for i in range(nn):
                    rollno = int(input("Enter Roll No:"))
                    name = input("Enter Name:")
                    unit1 = int(input("Enter unit1 marks:"))
                    unit2 = int(input("Enter unit2 marks:"))
                    unit3 = int(input("Enter unit3 marks:"))
                    unit4 = int(input("Enter unit4 marks:"))
                    unit5 = int(input("Enter unit5 marks:"))
                    assig1 = int(input("Enter Assignment 1 marks:"))
                    assig2 = int(input("Enter Assignment 2 marks:"))
                    midterm = int(input("Enter Midterm marks:"))
                    perlims = int(input("Enter perlims marks"))
                    total = unit1+unit2+unit3+unit4+unit5+assig1+assig2+midterm+perlims
                    w.writerow([rollno, name, unit1, unit2, unit3, unit4,
                               unit5, assig1, assig2, midterm, perlims, total])
        print("Written ")
    elif(n == 2):
        with open('marks.csv', "r") as f2:
            r = csv.reader(f2)
            data = list(r)
            for line in data:
                for word in line:
                    print(word, "\t", end="")
                print()
    else:
        break
