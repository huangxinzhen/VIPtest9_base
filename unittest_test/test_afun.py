# #测试用例类继承unittest.TestCase类
# import unittest
# from unittest_test import myfun
# class TestMyfun():
#     #初始化方法setUp  结束工作方法 tearDown
#     @classmethod
#     def setUpClass(cls):
#         print('setUpClass整个测试用例执行前执行一次')
#     def setUp(self):
#         print('setUp每条测试用例执行前执行一次')
#     #结束工作方法
#     @classmethod
#     def tearDownClass(cls):
#         print('tearDownClass整个测试执行后执行一次')
#     def  tearDown(self):
#         print('tearDown每条测试用例执行后执行一次')
#     #测试用例，方法以test开头
#     def test_add(self):
#         print('执行测试add方法')
#         #断言
#         self.assertEqual(myfun.add(1,2),3)
#     def test_minus(self):
#         print('执行minus方法')
#         self.assertEqual(2,myfun.minus(5,3))
#
# if __name__ == '__main__':
#     unittest.main()
#


# -*- coding: utf-8 -*-
'''
@Time    : 2021/2/6 16:24
@Author  : zxd
'''
#测试用例类继承unittest.TestCase类
import unittest

from unittest_test.myfun import *


class TestMyFun(unittest.TestCase):
    def test_div(self):
        print('执行测试div方法')
        self.assertEqual(2,divide(6,3))
if __name__ == '__main__':
    pass