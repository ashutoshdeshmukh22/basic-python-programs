from threading import *


def display():
    for i in range(5):
        print("Ashutosh")


t = Thread(target=display)  # creating Thread class
t.start()  # starting
for i in range(5):
    print("Swanand")
