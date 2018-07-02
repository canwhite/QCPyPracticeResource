#基本函数

print("============函数的一般例子，包含参数和返回值==========")

def sum(arg1,arg2):
    total = arg1 + arg2
    print("函数内:",total)
    return total

total =sum(2,3)
print("函数外:",total)



print("=========匿名函数:lambda arg1 ,arg2,... : expression")


#这种匿名函数的劣势就是只能写一行表达式
#这里add_value相当于函数名
add_value = lambda arg1,arg2 : arg1 + arg2

print("相加之后的值为:",add_value(10,20))


