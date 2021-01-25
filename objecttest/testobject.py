#-*-coding:utf-8 -*-
#1.定义一个类
class Washer():
    def __init__(self,width,height):
        """
        初始化功能函数
        :param width: 
        :param height: 
        """
        #属性
        # self.width = 200
        # self.height = 300
        self.width  = width
        self.height = height
    def __str__(self):
        """
        打印对象时默认返回return中的数据
        :return: 
        """
        return '这是海尔洗衣机的说明书'
    def __del__(self):
        """
        删除对象
        :return: 
        """
        print(f'{self}对象已经被删除')
    #方法
    def wash(self):
        print('我会洗衣服')
        print(self)
    def print_info(self):
        print(self.width, self.height)
#2.创建对象
haier1  =Washer(100,200)
# print(haier1)#打印对象在内存中的地址
haier1.wash()
# print(haier1)
# haier2 = Washer()
# print(haier2)
# haier1.width = 500
# haier1.height = 800
# print(haier1.width,haier1.height)
haier1.print_info()





