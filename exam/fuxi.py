#-*- coding:utf-8 -*-

# c = "I'm Tom"
# print(c)
# d = 'I\'m Tom'
# print(d)

# mystr = "hello world and superctest and chaoge and Python"
# print (mystr.find('and'))
# print (mystr.find('ands'))
# print (mystr.find('and',15,30))
# print (mystr.index('and'))
# print(mystr.count('and'))
# print(mystr.replace('and','heheda',2))
# print(mystr)
# print(mystr.split('and'))
# print(mystr.split('and'))
# my = mystr.split('and',2)
# print(my)
# list1 = []
# for i in range(len(my)):
#     list1 = '_'.join(my[i])
# print(list1)
#
# print(mystr.title())
# print(mystr.lower())
# print(mystr.upper())
# print(mystr.capitalize())

# mystr = "   hello world and superctest and chaoge and Python"

# print(mystr.lstrip())
# print(mystr.rstrip())
# print(mystr.strip()) #删除2测的空白
#
# print(mystr.ljust(60,'*'))
# print(mystr.rjust(60,'#'))
# print(mystr.center(60,'$'))
# print(mystr.endswith('and'))
# print(mystr.startswith(' '))
# mystr = 'pty123;'
# # print(mystr.isalpha())
# print(mystr.isalnum())

# mystr = 'srered;\'124444'
# print(mystr.isalnum())
# mystr = '143df2343'
# print(mystr.isdigit())
# mystr = '2 '
# print(mystr.isspace())
# a = 1
# b = 2
# c = a if a > b else b
# print(c)

# name_list = ['Tom','Lily','Rose','Rose']
# print(name_list[0])
# print(name_list.index('Lily',0,2))
# print(name_list.count('Rose'))
# print(len(name_list))
# print('lucy' in name_list)
# print('lucy' not in name_list)
# name_list.append('wangcai')
# print(name_list)
# # name_list.extend('xiaohong')
# print(name_list)
# name_list.extend(['xiaohai','xiaohong'])
# print(name_list)
# name_list.insert(0,'cc')
# print(name_list)
# name_list.insert(3,'tt')
# print(name_list)
# del name_list[0]
# print(name_list)
# name_list.pop()
# print(name_list)
# name_list.remove('Tom')
# print(name_list)
# name_list.remove('Rose')
# print(name_list)
# name_list.clear()
# print(name_list)
# name_list[-1] = 'xiaohei'
# print(name_list)
# name_list = [1,0,3,4,3,5,6,]
# print(name_list)
# name_list.reverse()
# print(name_list)
# name_list.sort()
# print(name_list)
# name_list.sort(reverse=True)
# print(name_list)
# list2 = name_list.copy()
# print(list2)


# name_list = ['Tom','Lily','Rose','Rose']
#
# for i in name_list:
#     print(i)
# print('##########')
# for i in range(len(name_list)):
#     print(name_list[i])

# str1 = '￥234857.3元9'
# a = str1.replace('￥','').replace('元','')
# print(a)



# name_list = ['Tom','Lily','Rose','Rose']
# name_list.remove('lily')
# print(name_list)

# name_list.clear()
# print(name_list)
# name_list[0] = 'xiaoxingxing'
# print(name_list)
# name_list = [['小明', '小红', '小绿'], ['Tom', 'Lily', 'Rose'], ['张三', '李四', '王五']]
#
# print(name_list[0][1])

# t1 = (10,20,30,20)
# print(type(t1))
# print(t1[0])
#
#
# print(t1.index(20))
# print(t1.count(20))
# print(len(t1))
# t1[10] = 1000

# tuple2 = (10, 20, ['aa', 'bb', 'cc'], 50, 30)
# tuple2[2][1] = 'aaaaa'
# print(tuple2)
# dict1 = {'name':'Tom','age':20,'gender':'男'}
# print(dict1.keys())
# print(dict1.values())
# name = input('input name:')
# for i in range(len(dict1)):
#     if dict1['name'] == name:
#         print('name is exit')
#         break
# for name in dict1.values():
#     print('name is exit')
# dict1 = {'name':'Tom','age':20,'gender':'男'}
# print(dict1['age'])
#
# del dict1['gender']
# print(dict1)
# # dict1.clear()
# # print(dict1)
# dict1['gender'] = '变性人'
# print(dict1)

# dict1 = {'name':'Tom','age':20,'gender':'男','name1':'小红'}

# print(dict1['age'])
# # print(dict1['sansui'])
#
# print(dict1.get('name'))
# print(dict1.values())
# print(dict1.get('name1'))
# print(dict1.items())
# dict1 = {'name':'Tom','age':20,'gender':'男','name1':'小红'}
# for key in dict1.keys():
#     print(key)
# for value in dict1.values():
#     print(value)
# for item in dict1.items():
#     print(item)
# for key,value in dict1.items():
#     print(f'{key} = {value}')

# s1 = {10,20,30}
# print(s1)
# s2 = {1,2,3,7,4,5,6}
# print(s2)
# s3 = set('abdbcd')
# print(s3)
# s4 = set()
# print(s4)
# s5 = {}
# print(s5)
# print(type(s5))
# age = 17.99
# if age >= 18:
#     print('已成年，可以上网')
# else:
#     print('小屁孩赶紧回家写作业')

# age = float(input('请输入年龄：'))
# if 18 <= age <= 60:
#     print('合法用工')
# elif age < 18:
#     print('非法使用童工')
# else:
#     print('法定退休年龄')



# import random
# ra = random.randint(0,2)
# print(ra)

# s1 = {10,20}
# s1.update([100,200])
# print(s1)
# s1.update('abc')
# print(s1)
# s1.update(['abc'])
# print(s1)
# s1 = {10,20}
# s1.remove(10)
# print(s1)
# s1.update(['xiaoxingxing'])
# print(s1)
# s1.discard(10)
# print(s1)

# s1 = {10,20,'xiaohai','heheda'}
# a = s1.pop()
# print(a)
# print(s1)
# for i in s1:
#     print(i)
# list1 =['hello']
# print(list1*4)
# t1 = ('world',)
# print(t1*4)

# str1 = 'abcdedd'
# print(len(str1))
#
# list1 = [10,20,30,40]
# print(len(list1))
# t1 = (10,20,30,40,50)
# print(len(t1))

# s1 = {10,20,40}
# print(type(s1))
# print(len(s1))

# dict1 = {'name':'Tom','age':20}
# print(len(dict1))

# str1 = 'abcdef'
# print(str1[0])
# del (str1[0])
# del str1
# print(str1)
# for i in range(len(str1)):
#     # del str1[i]
#     print(str1)
# list1 = [10,20,30,40]
# del(list1[0])
# print(list1)
# name_list = ['Tom','lily','rose']
# del_name = name_list.pop(0)
# print(del_name)
#
# name_list.clear()
# print(name_list)

# name_list.reverse()
# print(name_list)
# list1 = [10,20,30,40]
# print(max(list1))
# print(min(list1))
# str1 = 'abcdef'
# print(max(str1))
# print(min(str1))
# from time import sleep
# # for i in range(4):
# #     print('媳妇儿，我错了')
# #     print(i)
# #     sleep(1)
#1.循环计数器
# i = 0
# #2.循环条件
# while i < 5:
#     #3.循环体
#     print('媳妇儿，我错了')
#     #4.循环变量发生变化
#     i += 1
# print('任务结束')
#1.存变化的数
# i = 100
# #2.存和
# num = 0
# while i > 0:
#     if i % 2 == 0:
#         num += i
#     i -= 1
# print(num)

# num = 3
# while num > 0:
#     n = 0
#     while n < 5:
#         print('媳妇儿，我错了')
#         n += 1
#     print('刷晚饭的碗')
#     num -= 1
# n = 0
# while n < 5:
#     i = 0
#     while i < 5:
#         print('*',end='')
#         i += 1
#     print()
#     n += 1
#while循环的最后2个题目（1-三角形，2-99乘法表做作业）


# str1 = 'itheima'
# for i in str1:
#     if i == 'e':
#         print('遇到e不打印')
#         # break
#         continue
#     print(i)

# name_list = ['Tom','Lily','Rose']
# name = input('请输入您要搜索的名字：')
# if name in name_list:
#     print(f'您输入的名字是{name}，已经存在')
# else:
#     print(f'您输入的名字是{name}，不存在')
#     name_list.append(name)
# print(name_list)
#
# name_list.extend(['yy','xx'])
# print(name_list)
# name_list.extend('pop')
# print(name_list)


# name_list = ['Tom', 'Lily', 'Rose', 'mm', 'yy', 'xx', 'p', 'o', 'p']
# i = 0
# while i < len(name_list):
#     print(name_list[i])
#     i += 1
# for i in name_list:
#     print(i)
# print(name_list)
# name_list.reverse()
# print(name_list)
# name_list.sort(reverse=True)
# print(name_list)
# name_list.sort(reverse=False)
# print(name_list)

# name_list.pop(1)
# print(name_list)

# name_list = [['小明', '小红', '小绿'], ['Tom', 'Lily', 'Rose'], ['张三', '李四', '王五']]
# for i in name_list:
#     for j in i:
#         if j == '小i':
#             print('找到啦')
#             # break
#         else:
#             print('您要找的人不在')
#             break
#     break

# tuple1 = (['小明', '小红', '小绿'], 'Tom', 'Lily', 'Rose', ['张三', '李四', '王五'])
# key1 = str(input('请输入一个元素：'))
# if key1 in tuple1:
#     print(tuple1.count(key1))
# else:
#     print(f'元素不存在')

# for i in set1:
#     for j in i:
#         if j == '李i':
#             print('李i存在')
#         else:
#             i.append('李i')
#             break
#     break
# print(set1)

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{j} * {i} =',i*j,end='\t')
#     print()

# i = 1
# while i <= 100:
#     if i % 3 == 0:
#         print(i,end='\t')
#     i += 1
"""
list1 = [1,1]
c = list1[-1] + list1[-2]
"""

# list1 = [1,1]
# m = 1
# n = int(input('please input your number:'))
# while m <= n-2:
#     num = list1[-1] + list1[-2]
#     list1.append(num)
#     m += 1
# print(list1)

# num = int(input('input your num:'))
# n = 2
# while n < num:
#     if num % n == 0:
#         print('num不是质数')
#         break
#     n += 1
# else:
#     print(f'{num}是质数')
# a = 1
# b = 2
# tmp = a
# a = b
# b = tmp
# print(a,b)

# str1 = 'abcdefg'
# str1 = list(str1)
# print(type(str1))
# n = 0
# while n < len(str1)/2:
#     tmp = str1[n]
#     str1[n] = str1[len(str1)-n-1]
#     str1[len(str1) - n-1] = tmp
#     n += 1
# print(str1)
# for i in str1:
#     print(i,end='')
# print()
# print(''.join(str1))

# dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# dict1['name'] = 'Rose'
# print(dict1)
# dict1['id'] = 110
# print(dict1)

# dict1 = {'name': 'Rose', 'age': 20, 'gender': '男', 'id': 110}
# del dict1['name']
# print(dict1)
# dict1.clear()
# print(dict1)
# dict1['fun'] = 'singing'
# print(dict1)
# print(dict1.get('age',110))
# print(dict1.get('fun1'))
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())

# dict1 = {'name': 'Rose', 'age': 20, 'gender': '男', 'id': 110}
# for key in dict1.keys():
#     print(key)
# for value in dict1.values():
#     print(value)
# for key,value in dict1.items():
#     print(f'{key} = {value}')
# for item in dict1.items():
#     print(item)


# str1 = 'aa'
# str2 = 'bb'
# str3 = str1 + str2
# print(str3)

# list1 = [1,3]
# list2 = [10,20]
# list3 = list1 + list2
# print(list3)
# t1 = (1,2)
# t2 = (10,20)
# t3 = t1 + t2
# print(t3)
# print('*'*10)
# list1 = ['hello']
# print(list1*4)
# t1 = ('world')
# print(t1*4)

# print('a' in 'abcd')
# print('a' not in 'abcd')
# list1 = ['a','b','c','d']
# print('a' in list1)
# print('a' not in list1)

# t1 = ('a','b','c','d')
# print('aa' in t1)
# print('aa' not in t1)

# str1 = 'abcdefg'
# print(len(str1))
# del str1
# print(str1)

# list1 = [10,20,30,40]
# del(list1[0])
# print(list1)

# list1 = ['a', 'b', 'c', 'd', 'e']
# for i in enumerate(list1):
#     print(i)
# for index,char in enumerate(list1,start=1):
#     print(f'下标是{index},对应的字符串是{char}')

# list1 = [10, 20, 30, 40, 50, 20]
# s1 = {100, 200, 300, 400, 500}
# print(tuple(list1))
# print(type(tuple(list1)))
# print(tuple(s1))

# list1 = [10, 20, 30, 40, 50, 20]
# t1 = ('a', 'b', 'c', 'd', 'e')
# print(set(list1))
# print(set(t1))
# list1 = [i for i in range(10) if i % 2 == 0]
# print(list1)
# set1 = {i for i in range(5) if i > 3}
# print(set1)
# list1 = [(i,j) for i in range(1,3) for j in range(3)]
# list2 = [[i,j] for i in range(1,3) for j in range(3)]
# list3 = [{i:j} for i in range(1,3) for j in range(3)]
# print(list1)
# print(list2)
# print(list3)

# list1 = ['name', 'age', 'gender']
# list2 = ['Tom', 20, 'man']
# dict1 = {list1[i]:list2[i] for i in range(len(list1))}
# print(dict1)
# counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
# counts1 = {key:value for key,value in counts.items() if value > 200}
# print(counts1)
# def add(*args):
#     print(*args)
# list1 = [1,2,3]
# add(list1)
# def add(**kwargs):
#     print(kwargs)
# list1 = '[1,2,3]'
# add(a = 1)
# add(list1 = '[1,2,3]')

# a = 100
# print(id(a))
# sum = 0
# for i in range(4):
#     sum += i
# print(sum)
# def sum_numbers(num):
#     #1.如果是1，直接返回1 --出口
#     if num == 1:
#         return 1
#     #2.如果不是1，重复执行累加并返回结果
#     return num + sum_numbers(num - 1)
# print(sum_numbers(3))
# def fib(num):
#     if num == 1 or num == 2:
#         return 1
#     return fib(num - 1) + fib(num -2)
# print(fib(3))
# print(fib(4))
# print(fib(5))
# print(fib(6))
# for i in range(1,6):
#     print(fib(i),end='\t')




# for i in range(4):
#     print(fib(i))




# def fn1():
#     return 200
# print(fn1())
# print(fn1)


# x = lambda :200
# print(x())
# print(x)


# fn1 = lambda a,b:a+b
# print(fn1(1,2))
# fn1 = lambda a:a
# print(fn1('hello world'))

# fn1 = lambda a,b,c = 100: a + b + c
# print(fn1(2,3))

# fn1 = lambda *args:args
# print(fn1(10,20,40))
# print(fn1([10,20,40]))
#
# fn2 = lambda **kwargs:kwargs
# print(fn2(name = 'python',age = 20))

# fn1 = lambda a,b:a if a >b else b
# print(fn1(-1,2))
# students = [
#  {'name': 'TOM', 'age': 20},
#  {'name': 'ROSE', 'age': 19},
#  {'name': 'Jack', 'age': 22} ]
#
# students.sort(key = lambda x:x['name'])
# print(students)
#
# students.sort(key=lambda x:x['age'],reverse=True)
# print(students)
# students.sort(key=lambda x:x['age'])
# print(students)

# dict1 = {'a':1,'b':2,'c':3}
# def add(**kwargs):
#     print(kwargs)
# add(**dict1)
# list1 = [2,4,9,6,0,5]
# list1.sort(key=lambda x:x,reverse=True)
# list1.sort(key=lambda x:x,reverse=False)
#
# print(list1)

# list1 = [1,2,3,4,5]
# list1 = {1,2,3,4,5}
# def fun(x):
#     return x**2
# result = map(fun,list1)
# print(result)
# print(list(result))

# import functools
# list1 = [1,2,3,4,5]
# def func(a,b):
#     return a + b
# result = functools.reduce(func,list1)
# print(result)

# list1 = [1,2,3,4,5,6,7,8,9,10]
# def func(x):
#     return x % 2 == 0
# result = filter(func,list1)
# print(result)
# aa = list(result)
# print(aa)

# file = open('data.txt','r')
# file.close()
# with open() as f:
#     f.read()


# f = open('test.txt')
# content = f.readline()
# print(f'第一行：{content}')
#
# content = f.readline()
# print(f'第二行：{content}')
# content = f.readlines()
# f.close()
# print(len(content))
# print(content)
# list1 = []
# for i in range(len(content)):
#     # i.strip('\n')
#     # list1.append(i)
#     # print(list1)
#     str1 = content[i].strip('\n ')
#     print(str1)
#     list1.append(str1)
# print(list1)

# list1 = []
# for i in content:
#     # str1 = i.strip('\n')
#     # list1.append(str1)
#     # print(list1)
#     i.strip('\n')
#     # print('~~~~',i)
#     # print('####',str1)
#     list1.append(i)
# print(list1)
"""
需求：文件备份，将data.txt的文件备份
分析：
    1.打开data.txt文件 f1 = open('dataY.txt','r')
    2.读data.txt文件的内容readlines()
    3.创建一个新文件data_backup.txt，f2 = open('data_backup.txt','w')
    4.将第二步骤读取出来的内容写入到新文件中，f2.write()
        4.1 通过for循环遍历readlines读取出来的列表
            f2.write(i)
"""
from time import sleep

f = open('dataY.txt', 'r', encoding='utf-8')
f1 = open('data_backup.txt', 'w', encoding='utf-8')
n = 1
while True:
    content = f.read(1024)
    # f.close()
    # print(content)
    # print(len(content))
    print(content)
    if len(content) == 0:
        print('已备份完成')
        break
    f1.write(content)
    print('n:',n)
    n += 1
f.close()
f1.close()




# f = open('data.txt','r')
# list1 = f.readlines()
# f.close()
# print(len(list1))
# print(list1)
# name = input('input:')
# for i in range(len(list1)):
#     list2 = eval(list1[i])
    # print(list2,type(list2))
    # print(len(list2),list2[0],list2,type(list2[0]))
    # for i in range(len(list2)):
    #     if list2[0] == name:
    #         print(f'you {name}')
    #         break
    # else:
    #     list0 = []
    #     list0.append(name)
    #     str1 = str(list0)
    #     f = open('data.txt','a')
    #     f.write(str1)
    #     f.close()
    #     break
    # list3 = list1[i]
    # list2 = eval(list1[i])
    # print('list2:',len(list2),type(list2),list2)
    # for i in eval(list1[i]):
    #     print(i)
    #     if i == 'lily':
    #         print('you lily')
    #     break
    # break









