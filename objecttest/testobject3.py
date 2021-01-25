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
#徒孙类
class Tusun(prentice):
    pass


# xiaoming = prentice()
# xiaoming.make_cake()
# xiaoming.make_master()
# xiaoming.make_school()
xiaogang = Tusun()
xiaogang.make_cake()
xiaogang.make_school()




