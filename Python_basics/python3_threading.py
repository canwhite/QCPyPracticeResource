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

class MyThread(threading.Thread):

    


    #构造函数带参
    def __init__(self,threadID,name,delay):
        #线程初始化
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
        self.threadLock = threading.Lock()
        



    #run方法是重写的，调用start方法，run方法就会被调用，run方法代表了线程活动的方法
    # start方法开始线程活动。
    # 对每一个线程对象来说它只能被调用一次，它安排对象在一个另外的单独线程中调用run()方法（而非当前所处线程）
    def run(self):

        print("开始线程" + self.name)
        total = 5

        delay = self.delay

        threadName = self.name
        #这里调用方法一定要使用self，要不然会报NameError的错误
        self.print_time(self.name,self.delay,5)

    
    
        
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


    thread1.start()
    thread2.start()


    #join的作用是，在子线程完成动作之前，阻塞父线程
    thread1.join()
    thread2.join()

    print("退出线程")































































