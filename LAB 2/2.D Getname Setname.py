
from threading import *
print(current_thread().getName())
current_thread().setName("Ashutosh ")  # to set our own name by programmer
print(current_thread().getName())  # returns name of the thread
