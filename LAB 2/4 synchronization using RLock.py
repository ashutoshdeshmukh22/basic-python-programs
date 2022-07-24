from threading import *
I = RLock()


def factorial(n):
    I.acquire()
    if n == 0:
        result = 1
    else:
        result = n*factorial(n-1)
    I.release()
    return result


def results(n):
    print("The factorial of", n, "is:", factorial(n))


t1 = Thread(target=results, args=(4,))
t2 = Thread(target=results, args=(3,))
t1.start()
t2.start()
