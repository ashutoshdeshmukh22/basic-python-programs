from cgitb import reset
from threading import *
import time
from unittest import result

I = RLock()


def factorial(n):
    I.acquire()
    if n == 0:
        result = 1
    else:
        result = n * factorial(n-1)
    I.release()
    return result


def results(n):
    print("The Factorial of ", n, " is ", factorial(n))


t1 = Thread(target=results, args=(5,))
t2 = Thread(target=results, args=(9,))
t1.start()
t2.start()
