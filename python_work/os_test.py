import os
import sys



#pre 问答提示:
#========1.建议自己在桌面建一个py文件，尝试一下========



#========2.os模块和sys模块的区别=========
#os模块负责程序与操作系统的交互，提供了访问操作系统底层的接口;sys模块提供了一系列有关Python运行环境的变量和函数，更多的是环境信息



#========3.文件和目录的区别==========
#目录是由一层层的文件夹组成的,mkdir创建的就是目录
#目录中的内容 eg: test.py 这就是文件


#========4.cwd========

#current work  dir  当前的工作目录




#$$$$$$$$$$$$$$$$$$$$$$$   第一部分：os  $$$$$$$$$$$$$$$$$$$$$$$$


#了解：os.name nt 表示window    posix 表示linux
print(os.name)#result: posix



'''(1)当前路径和文件'''
#1.返回当前工作目录,即文件所在目录——os.getcwd()
print(os.getcwd())#result :/Users/ericzhang/Desktop/python_work



#返回目录下所有文件列表——os.listdir(path)
path = os.getcwd()
#print(os.listdir(path))






'''(2)绝对路径'''
#绝对路径 os.path.abspath(path)
print(os.path.abspath(os.getcwd()))#result:/Users/ericzhang/Desktop/python_work








'''(3)查看文件名或目录'''
#将path的目录和文件名分开成元组,前一个是路径，后一个是文件名

print(os.path.split(os.getcwd()))#result :('/Users/ericzhang/Desktop', 'python_work')


#将path1和path2进行组合，若path2是绝对路径则path1被删除，实际上直接用+拼接也可以

print(os.path.join(os.getcwd(),'pycrypto'))#结果/Users/ericzhang/Desktop/python_work/pycrypto


#返回path中的目录，返回的是父级目录，windows结果不包含"\",用的是mac，对应的是"/"

print(os.path.dirname(os.getcwd()))#result /Users/ericzhang/Desktop
print(os.getcwd()) #mac上 result ： /Users/ericzhang/Desktop/python_work
print(os.getcwd().replace('/','\\'))  #mac 转 windows  result：\Users\ericzhang\Desktop\python_work


#返回path中的文件名

print(os.path.basename(os.getcwd()))  #result: python_work








'''(4)创建目录'''
#创建path目录，只一级
#os.mkdir('test_makedir') #result，在当前脚本所在的文件夹，创建了test_makeDir文件
#os.mkdir("test_remove") #在创建一个，带着上边这个，后面测试remove的时候用

#创建path目录们，多级
#os.makedirs('test_mkdirs_out/test_mkdirs_in') #result : 在当前脚本所在的文件夹，创建了test_mkdirs_out，然后在其内部创建了test_mkdirs_in





'''(5)删除文件和目录'''

#删除文件（必须是文件，）
#os.remove('test.py')

#删除path目录（只能删除一级目录）
#os.rmdir('test_makedir') # 当前脚本所在文件夹中，test_makedir文件夹被删除

#删除多级别目录

#os.removedirs('test_mkdirs_out/test_mkdirs_in')#当前脚本所在文件夹中，test_mkdirs_out和它的子文件test_mkdirs_in 被删除






'''(6)更改路径'''
#  将当前工作目录，更好为指定路径
'''更换路径'''
#os.chdir('/Users/ericzhang/Desktop/chdir_test2')
#print(os.getcwd())#result:/Users/ericzhang/Desktop/chdir_test2
#details: 我在桌面上创建了两个文件，一个chdir_test1,一个chdir_test2, 在一中使用以上方法，路径被置换，指针指向同一个文件夹





'''(7)查看文件时间'''

#返回文件或目录的最后修改时间，结果为秒数
print(os.path.getmtime(os.getcwd())) #result:1522030564.0


#返回文件或目录的最后访问时间，结果为秒数
print(os.path.getatime(os.getcwd()))#result :1522031394.0


#返回文件或目录的创建时间，结果为秒数

print(os.path.getctime(os.getcwd())) #result : 1522030564.0






'''(8)查看文件大小'''

#返回文件的大小，若是目录则返回0
file_base_dir = os.getcwd() + '/os_test.py'#方便下边查看目录或者文件是否存在的使用
print(os.path.getsize(file_base_dir))  #result：3800








'''(9)查看目录或者文件是否存在'''

#判断path是否存在，存在返回true，不存在返回false
print(os.path.exists(os.getcwd())) #result : True


#判断path是否为文件，是返回为true，不是返回为false
#print(os.path.isflie(file_base_dir)) #没找到这个方法


#判断path是否是目录，是返回true，不是的话返回 false

print(os.path.isdir(os.getcwd()))  #result ： True





'''(10)表现形式参数'''

#返回当前操作系统，特定的路径分割符

print(os.sep)# result ： ／

#返回当前平台使用的行终止符
print(os.linesep)

#返回文件名和拓展名的分割符
print(os.extsep)




'''(11)递归返回path下的目录，包含path目录、子目录、文件名的三元组'''

print(os.walk(path))  #result  <generator object walk at 0x10757b1a8> 一个地址





#$$$$$$$$$$$$$$$$$$$  第二部分： sys    $$$$$$$$$$$$$$$$$$$$$$$$$

#(1)sys.argv
'''
获取当前正在执行的命令行参数的参数列表
sys.argv[0]  当前程序名
sys.argv[1]  第一个参数
sys.argv[2]  第二个参数

'''


print('sys.argv:%s' %(sys.argv)) #result:sys.argv:['/Users/ericzhang/Desktop/python_work/os_test.py']

print('sys.argv[0]:%s' %(sys.argv[0]))#result:/Users/ericzhang/Desktop/python_work/os_test.py

#print('sys.argv[1]:%s' %(sys.argv[1]))#result: IndexError: list index out of range  表示没有这个参数


#(2)sys.platform

'''

获取当前执行环境的平台,其中win32表示是windows 32bit操作系统，linux2表示是linux平台

'''

print('platform:%s' %(sys.platform)) #resutl: darwin 表示macosx




#(3)sys.path

'''
path  是一个目录列表，供python查找第三方拓展模块

'''


print('sys.path:%s'%(sys.path))#result:['/Users/ericzhang/Desktop/python_work', '/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Version...]


#在path的开始位置，插入test，然后就可以导入test import test

sys.path.insert(0,'time_test')
print(sys.path)
#result ['time_test', '/Users/ericzhang/Desktop/python_work', '/usr/local/...]
#然后我们就可以导入sys_test, 当然前提是我们文件中要有这个存在
import time_test

#result : 这个文件被执行了，
'''当前时间戳:1522042242.830849
日期格式:2018-03-26 13:30:42
time.struct_time(tm_year=2018, tm_mon=3, tm_mday=26, tm_hour=13, tm_min=30, tm_sec=42, tm_wday=0, tm_yday=85, tm_isdst=0)
[Finished in 0.1s]
'''



#另外一种添加自定义模块的方法：sys.path.append('module名字')
sys.path.append('count')
print(sys.path)

import count
'''
result:
['time_test', '/Users/ericzhang/Desktop/python_work', ..., 'count']

当前时间戳:1522044025.7241302
日期格式:2018-03-26 14:00:25
time.struct_time(tm_year=2018, tm_mon=3, tm_mday=26, tm_hour=14, tm_min=0, tm_sec=25, tm_wday=0, tm_yday=85, tm_isdst=0)

'''



#(4)sys.builtin_module_names

'''

返回一个列表，包含内建模块的名字,这些模块都是我们可以使用的

'''

print(sys.builtin_module_names)


'''
result:
('_ast', '_codecs', '_collections', ...,'pwd', 'sys', 'time', 'xxsubtype', 'zipimport')

'''



#(5)sys.exit(n)

'''

调用sys.exit(n)可以中途退出程序，当参数非0的时候，会导致SystemExit异常，从而可以在主程序中捕获该异常

效果：最少不会系统报错

'''

print('runing.....')
try:
    sys.exit(1)
except SystemExit:
    print("SystemExit Error")





















































































