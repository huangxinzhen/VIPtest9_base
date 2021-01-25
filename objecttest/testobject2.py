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
class prentice(Master):
    pass
xiaoming = prentice()
xiaoming.make_cake()

mst = Master()
mst.make_cake()


