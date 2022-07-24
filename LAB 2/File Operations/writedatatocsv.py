import csv
with open('movie.csv', "w", newline="") as f1:
    w = csv.writer(f1)
    w.writerow(["Category", "Winner", "Film", "Year"])
    n = int(input("Enter number of movies:"))
    for i in range(n):
        category = input("Enter category")
        winner = input("Enter winner")
        film = input("Enter filmname")
        year = input("Enter year")
        w.writerow([category, winner, film, year])
        print("Written successfully")
