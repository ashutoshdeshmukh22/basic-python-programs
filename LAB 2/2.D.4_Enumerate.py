# enumerate() function
# function which returns a list of all active threads currently running.

from threading import *
import time


def display():
    print(current_thread().getName(), "....started")
    time.sleep(3)
    print(current_thread().getName(), "....ended")


t1 = Thread(target=display, name="Ashutosh")
t2 = Thread(target=display, name="Swanand")
t3 = Thread(target=display, name="Vishal")
t1.start()
t2.start()
t3.start()
