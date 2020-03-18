#coding:utf-8
import os
#打印当前执行脚本所在目录
print(os.getcwd())
#如果当前路径存在则返回"True"，如果不存在则返回"False"
print(os.path.exists('/testDate/tt.png'))
#判断当前路径是否是一个文件，如果是则返回"True"，如果不存在则返回"False"
print(os.path.isfile('testData.xlsx'))
#创建文件夹
os.mkdir('testRm')
#创建多级文件夹
os.makedirs('./test/test01/test02')
#删除多级目录
os.removedirs("testRm")
os.removedirs('./test/test01/test02')

