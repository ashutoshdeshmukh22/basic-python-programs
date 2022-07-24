from threading import *
import time


def job():
    for i in range(5):
        print("Late Thread")
        time.sleep(2)


t = Thread(target=job)
# t.setDaemon(True) if we comment both the threads are non daemon and so they will executed until their completion
t.start()
time.sleep(5)
print("End Thread")
