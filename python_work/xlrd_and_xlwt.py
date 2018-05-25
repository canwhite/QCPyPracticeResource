#xlrd_and_xlwt.py
#文件位置
# /Users/ericzhang/Desktop/python_work/demo.xlsx
#-*- coding: UTF-8 -*-
import xlrd
import xlwt
from datetime import date,datetime



def read_excel():


    #打开文件
    workbook = xlrd.open_workbook(r'demo.xlsx')
    #获取所有sheet
    print(workbook.sheet_names())
    #获取第二个sheet的名字
    # sheet2_name = workbook.sheet2_names()[1]
    #两种方法获取sheet内容
    #(1)根据索引,从0开始的，我们要的是第二个
    sheet2 = workbook.sheet_by_index(1)
    #(2)根据名称获取sheet内容
    sheet2 = workbook.sheet_by_name('sheet2')
    #输出sheet的名称，行数，和列数
    print('name:%s\trows:%s\tcols:%s'%(sheet2.name,sheet2.nrows,sheet2.ncols))
    #获取整行和整列的值
    rows = sheet2.row_values(3) #获取第四行内容
    cols = sheet2.col_values(2) #获取第三列内容
    #获取单元格内容
    print(sheet2.cell(1,0).value.encode('utf-8'))# 用这一种
    print(sheet2.cell_value(1,0).encode('utf-8'))
    print(sheet2.row(1)[0].value.encode('utf-8'))
    #获取单元格内容的数据类型
    print(sheet2.cell(1,0).ctype)
    print('中文')



if __name__ == '__main__':
    read_excel()
