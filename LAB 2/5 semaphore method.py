from threading import *
import time
s = Semaphore(2)


def wish(name):
    s.acquire()
    for i in range(5):
        print("HEYYYY:", end='')
        time.sleep(2)
        print(name)
    s.release()


t1 = Thread(target=wish, args=("Ashutosh",))
t2 = Thread(target=wish, args=("Swanand",))
t3 = Thread(target=wish, args=("Shreyash",))
t4 = Thread(target=wish, args=("Gaurav",))
t5 = Thread(target=wish, args=("Vishal",))
t6 = Thread(target=wish, args=("Saurabh",))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
