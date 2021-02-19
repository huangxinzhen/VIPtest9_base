import unittest
import os
class RunAllCase():
    def run_test(self):
        #调用defaultTestLoad类中的discover方法,寻找测试集合
        #路径获取，当前文件：__file__
        test_dir = os.path.dirname(__file__)

        # suite = unittest.defaultTestLoader.discover('D:\\lc\\VIPtest9_base\\unittest_test',pattern='test*.py')
        suite = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
        #构造创建测试用例执行机器
        runner = unittest.TextTestRunner()
        #4.运行测试用例集合
        runner.run(suite)
if __name__ == '__main__':
    RunAllCase().run_test()

