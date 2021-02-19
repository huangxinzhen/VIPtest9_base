#-*-coding:utf-8-*-

"""
1-课上的所有代码重新敲一遍
"""
# from  importtest import my_module1 as myM
# import math
# print(math.sqrt(9))
# from math import sqrt
# print(sqrt(9))

# from importtest import my_module1
# my_module1.print_info()

# from my_module1 import *
# print_info()

# class Dog(object):
#     def work(self):
#         print('指哪打哪。。。')
#     def workdog(self):
#         print('你是一只爱工作的狗狗。。。')
# class DrugDog(Dog):
#     def work(self):
#         print('追查毒品。。。')
#     def workdog(self):
#         print('你是一只爱工作的狗狗。。。')
# class ArmyDog(Dog):
#     def work(self):
#         print('追击敌人。。。')
#
# class Person(object):
#     def work_with_dog(self,dog):
#         dog.work()
# ad = ArmyDog()
# dd = DrugDog()
#
# daqiu = Person()
# daqiu.work_with_dog(ad)
# daqiu.work_with_dog(dd)


# class Dog(object):
#     tooth = 10
# wangcai = Dog()
# xiaohei = Dog()
# print(wangcai.tooth)#实例对象访问
# print(xiaohei.tooth)
# print(Dog.tooth)#类对象访问
"""
类属性只能通过类对象修改，不能通过实例属性修改，如果通过实例对象
修改属性，表示创建了一个实例属性
"""
# class Dog(object):
#     tooth = 10
#
# wangcai = Dog()
# xiaohei = Dog()
#
# #修改类属性
# Dog.tooth = 12
# print(wangcai.tooth)
# print(xiaohei.tooth)
# print(Dog.tooth)
#
# #不能通过实例对象修改属性，如果是这样操作，实则是创建了一个实例属性
# wangcai.tooth = 20
# print(Dog.tooth)
# print(wangcai.tooth)
# print(xiaohei.tooth)

# class Dog(object):
#     def __init__(self):
#         self.age = 5
#
#     def info_print(self):
#         print(self.age)
# # print(Dog.age)
# wangcai = Dog()
# print(wangcai.age)
# wangcai.info_print()

"""
当方法中需要使用类对象（如访问私有类属性等）时，定义类方法
类方法一般和类属性配合使用
"""
# class Dog(object):
#     __tooth = 10
#     @classmethod
#     def get_tooth(cls):
#         return cls.__tooth
# wangcai = Dog()
# res = wangcai.get_tooth()
# print(res)

"""
静态方法：
需要通过装饰器@staticmethod来进行修饰，静态方法既不需要传递类对象，
也不需要传递实例对象（形参没有self/cls）

静态方法也能够通过实例对象和类对象去访问

使用场景：
当方法中既不需要使用实例对象（如实例对象、实例属性），也不需要使
用类对象（如类属性、类方法、创建实例等）时，定义静态方法

取消不需要的参数传递，有利于减少不必要的内存占用和性能消耗
"""
# class Dog(object):
#     @staticmethod
#     def info_prinnt():
#         print('这是一个狗类，用于创建狗实例。。。')
# wangcai = Dog()
# #静态方法既可以使用对象访问又可以使用类访问
# wangcai.info_prinnt()
# Dog.info_prinnt()

"""
异常的写法
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
else:
    没有异常的时候执行的代码
finally:
    有没有异常都要执行的代码

"""
# try:
#     f = open('test.txt','r')
# except:
#     f = open('test.txt','w')

# try:
#     f = open('test.txt','r')
# except Exception as result:
#     print(result)

# try:
#     print(num)
# except NameError:
#     print(NameError,'有错误')

"""
捕获多个指定异常
当捕获多个异常时，可以把要捕获的异常类型的名字，
放到except后，并使用元组的方式进行书写
"""
# try:
#     print(2/0)
# except(NameError,ZeroDivisionError) as res:
#     print(res,'有错误')
"""
捕获异常描述信息
"""
# try:
#     print(num)
# except (NameError,ZeroDivisionError) as result:
#     print(result)

#异常的else，else表示的是如果没有异常要执行的代码
# try:
#     print(1)
# except Exception as result:
#     print(result)
# else:
#     print('我是else，是没有异常的时候执行的代码')


#异常的finally，表示的是无论是否异常都要执行的代码，例如关闭文件
# import time
# try:
#     f = open('test.txt')
#     try:
#         while True:
#             content = f.readline()
#             if len(content) == 0:
#                 break
#             time.sleep(2)
#             print(content)
#     except:
#         print('意外终止了读取数据')
# except Exception as result:
#     print(result)
# else:
#     print('没有异常，真开心')
# finally:
#     f.close()

"""
在python中，抛出自定义异常的语法为raise异常对象
"""
#自定义异常类，继承Exception
# class ShortInputError(Exception):
#     def __init__(self,length,min_len):
#         self.length = length
#         self.min_len = min_len
#     #s设置抛出异常的描述信息
#     def __str__(self):
#         return f'你输入的长度是{self.length},不能少于{self.min_len}个字符'
# def main():
#     try:
#         con = input('请输入密码：')
#         if len(con) < 3:
#             raise ShortInputError(len(con),3)
#     except Exception as result:
#         print(result)
#     else:
#         print('密码已经输入完成')
# main()

#1.定义类
# class Wash():
#     def wash(self):
#         print('我会洗衣服')
#         print(self)
# #2.创建对象
# haier1 = Wash()
# print(haier1)
# #haier1对象调用实例方法
# haier1.wash()
#
# haier2 = Wash()
# print(haier2)
#
# haier1.width = 500
# haier1.height = 800

#定义类
# class Washer():
#     def print_info(self):
#         #类里面获取实物属性
#         print(f'haier1洗衣机的宽度是{self.width}')
#         print(f'haier1洗衣机的宽度是{self.height}')
# #创建对象
# haier1 = Washer()
# #添加实例属性
# haier1.width = 500
# haier1.height = 800
# haier1.print_info()

# class Washer():
#     #定义初始化功能的函数
#     def __init__(self):
#         #添加实例属性
#         self.width = 500
#         self.height = 800
#     def print_info(self):
#         #类里面调用实例属性
#         print(f'洗衣机的宽度是{self.width}，高度是{self.height}')
# haier1 = Washer()
# haier1.print_info()
#
# haier1.width = 1000
# haier1.height = 1400
# haier1.print_info()

#带参数的__init__
# class Washer():
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def print_info(self):
#         print(f'洗衣机的宽度是{self.width}')
#         print(f'洗衣机的高度是{self.height}')
#
# haier1 = Washer(100,300)
# # haier1.width = 100
# # haier1.height = 200
# haier1.print_info()

"""
__str__()
当使用print输出对象的时候，默认打印对象的内存地址。
如果类定义了__str__方法，那么就会从在这个方法中
return的数据
"""


# class Washer():
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def __str__(self):
#         return '这是海尔洗衣机的说明书'
#
# haier = Washer(10,20)
# print(haier)

"""
当删除对象时，python解释权也会默认调用__del__()方法
"""
# class Washer():
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def __del__(self):
#         print(f'{self}对象已经被删除')
# haier1 = Washer(1,2)
#
# del haier1
# print(haier1)
# class SweetPptato():
#     def __init__(self):
#         #被烤的时间
#         self.cook_time = 0
#         #地瓜的状态
#         self.cook_static = '生的'
#         #调料列表
#         self.condiments = []
#     def cook(self,time):
#         """烤地瓜的方法"""
#         self.cook_time += time
#         if 0<= self.cook_time < 3:
#             self.cook_static = '生的'
#         elif 3<= self.cook_time < 5:
#             self.cook_static = '半生不熟'
#         elif 5 <= self.cook_time < 8:
#             self.cook_static = '熟了'
#         elif self.cook_time >= 8:
#             self.cook_static = '烤糊了'
#     def add_condiments(self,condiment):
#         """添加调料"""
#         self.condiments.append(condiment)
#     def __str__(self):
#         return f'这个地瓜烤了{self.cook_time}分钟，状态是{self.cook_static}，添加的调料是{self.condiments}'
#
# digua1 = SweetPptato()
# digua1.cook(5)
# digua1.add_condiments('辣椒面')
# print(digua1)
#
# digua1.cook(2)
# print(digua1)
# digua1.cook(20)
# print(digua1)

# #家具类
# class Furniture():
#     def __init__(self,name,area):
#         #家具名字
#         self.name = name
#         #家具占地面积
#         self.area = area
# #房子类
# class Home():
#     def __init__(self,address,area):
#         #地理位置
#         self.address = address
#         #房屋面积
#         self.area = area
#         #剩余面积
#         self.free_area = area
#         #家具列表
#         self.furniture = []
#
#     def __str__(self):
#         return f'房子坐落于{self.address}，占地面积{self.area},剩余面积{self.free_area},家具有{self.furniture}'
#
#     def add_furniture(self,item):
#         """容纳家具"""
#         if self.free_area >= item.area:
#             self.furniture.append(item.name)
#             self.free_area -= item.area
#         else:
#             print('家具太大，剩余面积不足，无法容纳')
#
# bed = Furniture('双人床',6)
# jia1 = Home('北京',1200)
# print(jia1)
# jia1.add_furniture(bed)
# print(jia1)
#
# sofa = Furniture('沙发',10)
# jia1.add_furniture(sofa)
# print(jia1)

#面向对象-继承
#子类默认继承父类所有的方法和属性
#父类A
# class A(object):
#     def __init__(self):
#         self.num = 1
#     def info_print(self):
#         print(self.num)
# #子类B
# class B(A):
#     pass
# result = B()
# result.info_print()


#单继承，一个子类继承一个父类
# #1.师父类
# class Master(object):
#     def __init__(self):
#         self.kongfu = '[五香煎饼果子配方]'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# #2.徒弟类
# class Prentice(Master):
#     pass
# #3.创建对象xiaoming
# xiaoming = Prentice()
# #4.对象调用实例属性
# xiaoming.make_cake()
# #5.对象访问实例属性
# print(xiaoming.kongfu)

#多继承，一个类同时继承了多个父类
# class Master(object):
#     def __init__(self):
#         self.kongfu = '[五香煎饼果子配方]'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# #创建学校类
# class School(object):
#     def __init__(self):
#         self.kongfu = '[香辣煎饼果子配方]'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# #2.徒弟类
# #当一个类有多个父类的时候，默认使用第一个父类同名属性和方法
# class Prentice(Master,School):
#     pass
# xiaoming = Prentice()
# xiaoming.make_cake()
# print(xiaoming.kongfu)

#子类重写父类同名方法和属性
# class Master(object):
#     def __init__(self):
#         self.kongfu = '[五香煎饼果子配方]'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# #创建学校类
# class School(object):
#     def __init__(self):
#         self.kongfu = '[香辣煎饼果子配方]'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# #2.徒弟类
# #当一个类有多个父类的时候，默认使用第一个父类同名属性和方法
# class Prentice(Master,School):
#     def __init__(self):
#         self.kongfu = '[独创煎饼果子配方]'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
#
# xiaoming = Prentice()
# xiaoming.make_cake()
# print(xiaoming.kongfu)
# print(Prentice.__mro__)

#子类调用父类的同名方法和属性
# class Master(object):
#     def __init__(self):
#         self.kongfu = '[五香煎饼果子配方]'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# #创建学校类
# class School(object):
#     def __init__(self):
#         self.kongfu = '[香辣煎饼果子配方]'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# #2.徒弟类
# #当一个类有多个父类的时候，默认使用第一个父类同名属性和方法
# class Prentice(School,Master):
#     def __init__(self):
#         self.kongfu = '[独创煎饼果子配方]'
#     def make_cake(self):
#         """如果是先调用了父类的属性和方法，父类属性会覆盖子类属性，
#         故在调用属性前，先调用自己子类的初始化
#         """
#         self.__init__()
#         print(f'运用{self.kongfu}制作煎饼果子')
#     #调用父类方法，但是为保证调用的也是父类的属性，必须
#     #在调用方法前调用父类的初始化
#     def make_master_cake(self):
#         Master.__init__(self)
#         Master.make_cake(self)
#     def make_school_cake(self):
#         School.__init__(self)
#         School.make_cake(self)
# xiaoming = Prentice()
# xiaoming.make_cake()
# xiaoming.make_master_cake()
# xiaoming.make_school_cake()





#多层继承
# class Master(object):
#     def __init__(self):
#         self.kongfu = '[五香煎饼果子配方]'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# #创建学校类
# class School(object):
#     def __init__(self):
#         self.kongfu = '[香辣煎饼果子配方]'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# #2.徒弟类
# #当一个类有多个父类的时候，默认使用第一个父类同名属性和方法
# class Prentice(School,Master):
#     def __init__(self):
#         self.kongfu = '[独创煎饼果子配方]'
#     def make_cake(self):
#         """如果是先调用了父类的属性和方法，父类属性会覆盖子类属性，
#         故在调用属性前，先调用自己子类的初始化
#         """
#         self.__init__()
#         print(f'运用{self.kongfu}制作煎饼果子')
#     #调用父类方法，但是为保证调用的也是父类的属性，必须
#     #在调用方法前调用父类的初始化
#     def make_master_cake(self):
#         Master.__init__(self)
#         Master.make_cake(self)
#     def make_school_cake(self):
#         School.__init__(self)
#         School.make_cake(self)
# class Tusun(Prentice):
#     pass
# xiaogang = Tusun()
# xiaogang.make_school_cake()
# xiaogang.make_master_cake()


# #super()调用父类方法
# class Master(object):
#     def __init__(self):
#         self.kongfu = '[五香煎饼果子配方]'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# #创建学校类
# class School(object):
#     def __init__(self):
#         self.kongfu = '[香辣煎饼果子配方]'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# #2.徒弟类
# #当一个类有多个父类的时候，默认使用第一个父类同名属性和方法
# class Prentice(School,Master):
#     def __init__(self):
#         self.kongfu = '[独创煎饼果子配方]'
#     def make_cake(self):
#         """如果是先调用了父类的属性和方法，父类属性会覆盖子类属性，
#         故在调用属性前，先调用自己子类的初始化
#         """
#         self.__init__()
#         print(f'运用{self.kongfu}制作煎饼果子')
#     #调用父类方法，但是为保证调用的也是父类的属性，必须
#     #在调用方法前调用父类的初始化
#     def make_master_cake(self):
#         Master.__init__(self)
#         Master.make_cake(self)
#     def make_school_cake(self):
#         School.__init__(self)
#         School.make_cake(self)
#     def make_old_cake(self):
#         super().__init__()
#         super().make_cake()
# xiaoming = Prentice()
# xiaoming.make_old_cake()
# print(Prentice.__mro__)
#定义私有属性和方法
# class Master(object):
#     def __init__(self):
#         self.kongfu = '[五香煎饼果子配方]'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# #创建学校类
# class School(object):
#     def __init__(self):
#         self.kongfu = '[香辣煎饼果子配方]'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
# #2.徒弟类
# #当一个类有多个父类的时候，默认使用第一个父类同名属性和方法
# class Prentice(School,Master):
#     def __init__(self):
#         self.kongfu = '[独创煎饼果子配方]'
#         #定义私有属性
#         self.__money = 200000
#     #获取私有属性
#     def get_money(self):
#         return self.__money
#     #修改私有属性
#     def set_money(self):
#         self.__money = 500
#     #定义私有方法
#     def __info_print(self):
#         print(self.kongfu)
#         print(self.__money)
#     def make_cake(self):
#         """如果是先调用了父类的属性和方法，父类属性会覆盖子类属性，
#         故在调用属性前，先调用自己子类的初始化
#         """
#         self.__init__()
#         print(f'运用{self.kongfu}制作煎饼果子')
#     #调用父类方法，但是为保证调用的也是父类的属性，必须
#     #在调用方法前调用父类的初始化
#     def make_master_cake(self):
#         Master.__init__(self)
#         Master.make_cake(self)
#     def make_school_cake(self):
#         School.__init__(self)
#         School.make_cake(self)
#     def make_old_cake(self):
#         super().__init__()
#         super().make_cake()
#
# class Tusun(Prentice):
#     pass
# xiaoming = Prentice()
# xiaogang = Tusun()
# # xiaoming.__money
# # xiaoming.__info_print()
# print(xiaogang.get_money())
# xiaogang.set_money()
# print(xiaogang.get_money())
#
# print(xiaoming.get_money())

"""
2-http协议的组成，状态码含义；
答：http协议由请求和响应组成
2xx：200，请求成功，但不代表业务逻辑处理成功
3xx：重定向，请求的资源被分配的新的url，希望本次访问使用新的url
4xx：客户端错误，400为语法错误，403为forbidden拒绝，404为not found未找到
5xx：服务端错误，500为服务器内部错误，502为网关错误，504为网关超时
"""
"""
3-完成手机app抓包
"""
"""
4-get和post区别
答：1.安全：get安全性相比post比较低，post的安全性更好
    2.请求参数放的位置不同。get的请求参数放在url中，post的请求参数放在body中；
    3.提交内容限制的问题，get请求的参数长度有限制，表单可以发送更多内容的参数
"""
"""
5-cookie和session区别
答：1.存放的地方不一样，cookie存放在客户的浏览器上，session存放在服务器端；
    2.安全程度不同，cookie不是很安全，别人可以通过分析存在本地的cookie，进行cookie欺骗，考虑到安全，应该使用session；
    3.性能的使用程度不同，session会在一定的时间内保存在服务器上，当访问量增多的时候会占用服务器的性能，考虑到性能，应该使用cookie；
    4.存放数据的大小不同，单个cookie保存的数据不能超过4k，很多浏览器限制一个站点最多能保存20个cookie，
    而session则存于服务器端，浏览器对其没有限制；
    5.会话机制不同，session的会话机制是一种服务器断的机制，他使用类似于哈希表（可能还有哈希表）的结构来保存信息。
      cookie会话机制是服务器存储在本地的小块文本，并随每个请求发送到服务器端，web服务器端使用标头将cookie发送到客户端。
      在客户端，浏览器解析cookie并将其保存为本地文件，该文件自动将来自同一服务器的任何请求绑定到这些cookie。
"""
"""
6-预习request文档
"""
# import requests
# #发送get请求
# urlstr = 'https://www.wanandroid.com/'
# #发送请求
# r = requests.get(url=urlstr)
# print(r.text)

#发送get请求
# urlAndroid = 'https://www.wanandroid.com/article/query'
# #参数
# payload = {'k':'Android'}
# #2----发送请求
# r = requests.get(url=urlAndroid,params=payload)
# #获取结果
# print(r.text)
# print(r.status_code)


#请求百度首页
# r = requests.get('http://www.baiud.com/',verify=False)
# print(r.url)
# print(r.encoding)
# print(r.headers)
# print(r.cookies)
# print(r.content)

# print(r.json)
# print(r.raw)
# print(r.raise_for_status())

# help(requests)
# import json
# payload = dict(key1='value1',key2='value2')
# payload = json.dumps(payload)
# r = requests.post('https://htt[bin.org/post',data=payload)
# print(r.text)

# import requests
# urlstr = 'https://www.wanandroid.com/user/login'
# header = {'user-Agent':'Mozilla/5.0'}
# payload = {'username':'13246653227','password':'13246653227'}
# r = requests.post(url=urlstr,data=payload,headers = header)
# print(r.text)
# print('----',r.headers)
# print('11111',type(r.json()))
# print(r.json()['data']['username'])
# print(r.json()['data']['publicName'])
# print(r.json()['errorCode'])


