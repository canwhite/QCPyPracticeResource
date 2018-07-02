
import queue
import threading
import time


class MyThread (threading.Thread):
    def __init__(self, threadID, name,tLock):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.threadLock = tLock
        
        
        
        
    def run(self):
        print ("开启线程：" + self.name)
        
        workQueue = self.product()
        
        self.process_data(self.name, workQueue)
        print ("退出线程：" + self.name)


    def product(self):
        
        #把队列对象摆置好，方便在每个线程中输出
        #这个是先入先出
        nameList = ["One", "Two", "Three", "Four", "Five"]
        workQueue = queue.Queue(10)
        self.threadLock.acquire()
        for word in nameList:
            workQueue.put(word)
        self.threadLock.release()
        
        return workQueue


    def process_data(self,threadName, q):
        
        for i in range(q.qsize()):
            
            data = q.get()
            print ("%s processing %s" % (threadName, data))
            time.sleep(1)
            
            
            



if __name__ == "__main__":
    
    #队列对象，是需要我们传进去的
    threadList = ["Thread-1", "Thread-2", "Thread-3"]

    
    queueLock = threading.Lock()
    threadID = 1
    workQueue = queue.Queue(10)
    threads = []

    #for循环创建线程
    for tName in threadList:
        thread = MyThread(threadID, tName,queueLock)
        threads.append(thread)
        threadID += 1
        
    for t in threads:
        t.start()
        t.join()
        




# Python中，队列是线程间最常用的交换数据的形式。Queue模块是提供队列操作的模块，虽然简单易用，但是不小心的话，还是会出现一些意外。
#
# ===================pre:创建一个“队列”对象====================
# import Queue
# q = Queue.Queue(maxsize = 10)
# Queue.Queue类即是一个队列的同步实现。队列长度可为无限或者有限。可通过Queue的构造函数的可选参数maxsize来设定队列长度。如果maxsize小于1就表示队列长度无限。



# ===================(1)将一个值放入队列中=====================
# q.put(10)
# 调用队列对象的put()方法在队尾插入一个项目。put()有两个参数，第一个item为必需的，为插入项目的值；第二个block为可选参数，默认为
# 1。如果队列当前为空且block为1，put()方法就使调用线程暂停,直到空出一个数据单元。如果block为0，put方法将引发Full异常。



# ====================(2)将一个值从队列中取出==================
# q.get()
# 调用队列对象的get()方法从队头删除并返回一个项目。可选参数为block，默认为True。如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。如果队列为空且block为False，队列将引发Empty异常。



#====================(3)先进先出，先进后出和优先级队列===========
# Python Queue模块有三种队列及构造函数:
# 1、Python Queue模块的FIFO队列先进先出。     class Queue.Queue(maxsize)
# 2、LIFO类似于堆，即先进后出。                         class Queue.LifoQueue(maxsize)
# 3、还有一种是优先级队列级别越低越先出来。    class Queue.PriorityQueue(maxsize)



# ===================(4)此包中的常用方法(q = Queue.Queue())========
# q.qsize() 返回队列的大小
# q.empty() 如果队列为空，返回True,反之False
# q.full() 如果队列满了，返回True,反之False
# q.full 与 maxsize 大小对应
# q.get([block[, timeout]]) 获取队列，timeout等待时间
# q.get_nowait() 相当q.get(False)
# 非阻塞 q.put(item) 写入队列，timeout等待时间
# q.put_nowait(item) 相当q.put(item, False)
# q.task_done() 在完成一项工作之后，q.task_done() 函数向任务已经完成的队列发送一个信号
# q.join() 实际上意味着等到队列为空，再执行别的操作
      
        
            
    
    
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    










