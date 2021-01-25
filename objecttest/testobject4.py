# -*- coding:utf-8 -*-
# class A():
#     def __init__(self):
#         self.num  = 1
#     def info_print(self):
#         print(self.num)
#
# class B(A):
#     pass
# resut = B()
# resut.info_print()
#
class Master(object):
    def __init__(self):
        self.kongfu = '[五香煎饼果子]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
class School(object):
    def __init__(self):
        self.kongfu = '[香辣煎饼果子]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
class prentice(School,Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子]'
        self.__money = 20000
    def make_cake(self):
        #如果先调用父类的属性和方法，父类的属性方法会覆盖子类的属性方法，故先调用子类的初始化方法
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')
    def make_master(self):
        #调用父类方法，为了保证调用的是父类的属性，故先调用父类的初始化
        Master.__init__(self)
        Master.make_cake(self)
    def make_school(self):
        School.__init__(self)
        School.make_cake(self)
    def make_old_cake(self):
        #使用super()可以自动查找父类，调用顺序遵循__mro__类属性的顺序，比较适合单继承使用
        super().__init__()
        super().make_cake()
    #获取私有属性
    def get_money(self):
        return self.__money
    #修改私有属性
    def set_money(self):
        self.__money = 500
#徒孙类
class Tusun(prentice):
    pass

# pre = prentice()
# pre.make_old_cake()
# pre.make_cake()
# pre.set_money()
# print(pre.get_money())
xiaogang = Tusun()
xiaogang.make_cake()
xiaogang.set_money()
print(xiaogang.get_money())

