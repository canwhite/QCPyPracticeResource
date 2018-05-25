#文件和异常.py
#保存文件夹下的文件夹，或者是绝对位置
with open("text/my.txt") as file_object:
	# message = file_object.read()
	# print(message) 


	#逐行读取
	for msg in file_object:
		print(msg.rstrip())

#将文件内容储存在列表中

with open("text/my.txt") as file_object:

	lines = file_object.readlines()

#对列表中的数据进行使用
for line in lines:
	print( line.rstrip())




#包含百万位的大型文件pi_string[:52] pi_string是通过列表拼接好的字符串


#写入文件，  参数 读取模式 r 写入模式 w 附加模式 a 既能读取又能写入 r+，如果省略 默认为r

file_name = "readme.txt"
with open(file_name,"w") as file_object:
	file_object.write("i love you.\n" )
	file_object.write("i love me.\n")


#附加到文件。如果只是给文件附加内容 而不是覆盖，请用 a

with open(file_name,"a") as file_object:
	file_object.write("have loved.\n")
	file_object.write("....\n")



#异常的处理 

















