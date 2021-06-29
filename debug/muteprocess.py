import multiprocessing
import time
#后面的3是队列最多放3个
q = multiprocessing.Queue(3)
#多进程使用队列进行交换数据
def work1(q):
    for i in range(5):
        time.sleep(1)
        q.put("AA"+str(i))
def work2(q):
    for i in range(6):
        time.sleep(1)
        #加入过期参数来避免类死锁现象
        print("BB"+str(i)+"___"+q.get(timeout=2))
        #这里来一个取一个，所以就是0
        print("现在q里面还剩下%d个数据" % (q.qsize()))

def main_test():
    p1 = multiprocessing.Process(target=work1,args=(q,))
    p2 = multiprocessing.Process(target=work2,args=(q,))
    p1.start()
    p2.start()

if __name__ == '__main__':
    main_test()