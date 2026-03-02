import threading
import time

"""def mrn():
    for i in range(4):
        print("working....",i)
        time.sleep(4)
t=threading.Thread(target=mrn)
t1=threading.Thread(target=mrn)
t.start()
t.join()

t1.start()
t1.join()"""

"""counter=0
def incre():
    global counter
    for _ in range(10000):
        counter +=1

    

t=threading.Thread(target=incre)
t1=threading.Thread(target=incre)
t.start()
t1.start()
t1.join()
t.join()
print(counter)"""


counter=0
lock=threading.Lock()
def incre():
    global counter
    for _ in range(10000):
        lock.acquire()
        counter +=1
        lock.release()
    

t=threading.Thread(target=incre)
t1=threading.Thread(target=incre)
t.start()
t1.start()
t1.join()
t.join()
print(counter)