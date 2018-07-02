#列表

list1 = ["a","b","c","d"]
print("=================访问列表中的值 list[0]========================")
print("list1[0]:",list1[0])


print("=================更新list的值 list[0] = xxx===================")
list1[0] = "x"
print("list1[0]:",list1[0])


print("================删除list的某个值:del list[2]====================")

del list1[2]
print("删除掉c:",list1)


print("===============python列表函数===================================")
print("len(list)")
print("max(list)")
print("min(list)")

print("===============将元组转化成列表=================================")
aTuple = (123,"Google","Taobao","Weixin")
list2 = list(aTuple)
print("列表元素：" + str(list2))

str1 = "Hello World"
list3 = list(str1)
print("列表元素：" + str(list3))


print("==============python列表方法大全=============================")

#最后追加元素
list1.append("y")
print("append:",list1)

#移除最后一个元素

list1.pop()
print("pop:",list1)


#移除列表中某个值的第一个匹配项


#某个元素的个数
print("count:",list1.count("b"))


#某个位置添加某个值
list1.insert(4,"z")
print("insert:",list1)


#移除表中某个值的第一个匹配项

list1.remove("b")
print("remove:",list1)

#反向列表中的元素

list1.reverse()
print("reverse:",list1)


#对原列表进行排序
list1.sort()
print("sort:",list1)


list_copy = list1.copy()
print("copy:",list_copy)

#清空
list1.clear()
print("clear:",list1)





























































