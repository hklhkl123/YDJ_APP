import threading
mutex1 = threading.Lock()
x = 0
def ticket1():
    c1 = 0
    global x
    for i in range(100000):
        #这就是加锁后，形成了并发,blocking默认是True就是默认等待，改成False就会不等，但是锁不会被解除
        mutex1.acquire(blocking=True)
        x = x + 1
        mutex1.release()
    print("t1卖了，"+str(x))
def ticket2():
    c2 = 0
    global x

    for i in range(100000):
        mutex1.acquire()
        x = x + 1
        mutex1.release()
    print("t2卖了，"+str(x))

t1 = threading.Thread(target=ticket1)
t2 = threading.Thread(target=ticket2)
t1.start()
# t1.join()
t2.start()
