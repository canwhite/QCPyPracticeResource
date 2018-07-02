#python3_threading.py



# (1)写了一个Test类

import threading
import time


exitFlag = 0

# class Test:
#
#     def sing(self):
#         print("我输出了内容")
#
#     #调用本类方法的时候
#     def test(self):
#         self.sing()
        #当多个控制线程共享相同的内存时，需要确保每个线程看到一致的数据视图。如果每个线程使用的变量都是其他线程不会读取或修改的，那么就不会存在一致性问题。同样地，如果变量是只读的，多个线程同时读取该变量也不会有一致性问题。
    
#但是，当某个线程可以修改变量，而其他线程也可以读取或修改这个变量的时候，就需要对这些线程进行同步，以确保它们在访问变量的存储内容时不会访问到无效的数值。
    


class MyThread(threading.Thread):

    
    #构造函数带参
    def __init__(self,threadID,name,delay):
        #线程初始化
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
        self.threadLock = threading.Lock()
        
    
    
    def run(self):
        
        print("开启线程" + self.name)
        #获取锁，用于线程同步
        self.threadLock.acquire()
        
        self.print_time(self.name,self.delay,5)
        
        #释放锁，开启下一个线程
        self.threadLock.release()
   

        
    def print_time(self,threadName,delay,total):

        while total:
            if exitFlag:
                threadName.exit()

            time.sleep(delay)
            print("%s : %s " % (threadName,time.ctime(time.time())))
            total -= 1
        




if __name__ == '__main__':



    print("本类方法的连带调用记得使用self")
    
    
    thread1 = MyThread(1,"Thread-1",1)
    thread2 = MyThread(2,"Thread-2",2)


    #同步的时候，添加线程到线程列表
    threads = []
    threads.append(thread1)
    threads.append(thread2)
    
    
    #等待所有线程完成，join有阻塞父线程的作用
    #这是人为的加一个队列，我们在接下来会看到queue
    for t in threads:
         #开启新线程
        t.start()
        t.join()

    print("退出线程")




