#coding:utf-8
import xlwt
import os
wb = xlwt.Workbook()
sheet = wb.add_sheet("测试写入")
sheet.write(0,0,"第一个单元格数据")
sheet.write(0,1,"第二个单元格数据")
wb.save("测试数据写入.xlsx")
