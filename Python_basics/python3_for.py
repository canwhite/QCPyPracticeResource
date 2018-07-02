#for循环

languages = ["c","c++","perl","python3","oc"]


#for in

print("===============forin======================")
for x in languages:

    #c++跳过
    if x == "c++":
        continue;
    #oc跳出
    if x == "oc":
        break;

    
    print( x)
    
    


#range
print("================range(n)=====================")

for i in range(5):
    print(i)

print("===============range(m,n)====================")    
    

for i in range(5,9):
    print(i)

print("===============range(m,n,step)===============")

for i in range(1,8,2):
    print(i)

print("==============range(len(list))遍历索引================")
# len实际上是得到一个长度
for i in range(len(languages)):
    print(i,languages[i])


print("==============pass===========================")


while True:
    pass #等待键盘中断

#pass 不做任何事情，主要是一个占位语句

#eg：最小的类型

class EmptyClass:
    pass




    
    



