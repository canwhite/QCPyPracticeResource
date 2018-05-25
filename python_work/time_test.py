#time_test.py

import time

#当前时间戳
now_time = time.time()
print('当前时间戳:' + str(now_time) )

#转换成日期格式
#lo
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(now_time))
print('日期格式:' + str(otherStyleTime))

#了解一些localtime()方法
print(time.localtime())

