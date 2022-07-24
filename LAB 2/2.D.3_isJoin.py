from threading import *
import time


def display():
    for i in range(5):
        print("Ashutosh Deshmukh")
        time.sleep(2)


t = Thread(target=display)
t.start()
t.join(5)  # executed by main thread #t.join()for without time
for i in range(5):
    print("John Doe")
