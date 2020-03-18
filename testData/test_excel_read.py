#conding:utf-8
import xlrd
testDataPath = "testData.xlsx"
xls = xlrd.open_workbook(testDataPath)
#获取sheet的三种方法
#sheet = xls.sheets()[0]#通过sheets()方法获取sheet
#sheet2 = xls.sheet_by_name("sheet1")#通过sheet名字获取sheet
sheet3 = xls.sheet_by_index(0)#通过索引获取sheet
#打印表格总行数
print(sheet3.nrows)
#打印表格总列数
print(sheet3.ncols)
#打印表格第二行，第一列单元格值
print(sheet3.row_values(1)[0])
