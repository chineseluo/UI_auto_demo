#coding:utf-8
import unittest
import time
class Test1(unittest.TestCase):
    def setUp(self):
        print("开始执行脚本06")

    def tearDown(self):
        time.sleep(3)
        print("脚本06执行结束")

    def testf_01(self):
        print("开始执行第一个用例")

    def testf_02(self):
        print("开始执行第二个用例")

    def testf_03(self):
        print("开始执行第三个用例")

if __name__ == "__main__":
    unittest.main()
