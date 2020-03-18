#coding:utf-8
import ddt
import unittest

@ddt.ddt
class test_ddt(unittest.TestCase):
    def setup(self):
        pass
    @ddt.data(2,3,4)
    def test_01(self,t):
        print(t)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
