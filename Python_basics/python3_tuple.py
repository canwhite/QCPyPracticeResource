#元组

print("python 的元组和列表类似")
print("不同之处在于元组的元素不能修改")
print("元组用小括号，列表用方括号")

print("==========元组的创建=============================")

tup1 = ("a",1,"b","2")
tup2 = ("google","taobao","weixin")

print("tup1:",tup1)
print("tup2:",tup2)


print("==========访问方法和list的方法等同=================")

print("==========修改，只有一个两元组相加==================")

tup3 = tup1 + tup2
print("tup3:",tup3)



print("==========删除元组===============================")

del tup3;
#会提示该元素已经删除，不能修改
# print(tup3)



print("元组可以像列表一样： +  *  len()   【3 in (1,2,3) 判断是否存在 】 【for x in (1, 2, 3): print (x) 遍历】 ")



print("元组内置函数也和列表一样：len，max，min，以及列表转元组tuple(list)")










