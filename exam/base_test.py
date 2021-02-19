#-*-coding:utf-8

# """
# 解题思路：
# 1.自己调用自己
# 2.必须有出口
# 1 1 2 3 5 8 13 21 34...
#
# #定义一个函数
# 1.已知第一位和第二位上的书 1,1
# 2.当求第三位上的数时n，就让他前一位和前2位相加
# """
#
# x = int(input('please input the feibo number'))
# def fun(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fun(n-1) + fun(n-2)
# for i in range(1,x+1):
#     print(fun(i))

# list1 = ['1','2','3']
# list2 = [int(i) for i in list1]
# print(list2)


# """
# 解题思路：从未知的结果倒推到已知的条件
# 4.在全部得数据结果中查找年龄大于18的人名
#   3.在某一行的数据中查找年龄大于18的人名--拿到一行数据：‘lucy:21,tom:30’-->split逗号分隔==>'luct:21'-->split冒号分割拿到key和value
#   2.在某一组数据中查找年龄大于18的人名
#
#   1-文件io读取文件的内容，readelines(所有行组成一个列表，每一行作为一个元素)
#     [1,2,3]
# """
# f = open('data.txt','r')
# list1 = f.readlines()
# # print(list1)
# dict1 = {}
# for i in list1:
#     # print(i.strip())
#     list2 = i.strip().split(',')
#     for j in list2:
#         # print(j.split(':'))
#         list3 = j.split(':')
#         dict1[list3[0]]  = int(list3[1])
# # print(dict1)
# resultlist = []
# for i in dict1.keys():
#     # print(i,dict1[i])
#     if dict1[i] > 18:
#         resultlist.append(i)
# print(resultlist)

"""
解题思路：
   2.得到一行所有单词的翻转
   1.得到一行中某一个单词的翻转
        字符串首页翻转welcome-->emcolew-->a=1,b=2  c-->a,b=b,a
        str1[0],str[6]=str[6],str[0]
"""
# words = 'welocme to super&Test'
# list1 = words.split(' ')
# # print(list1)
# # for i in range(len(list1))
# def fun(item):
#     strlist = list(item)
#     # print(strlist)
#     for i in range(len(strlist)):
#         if i < len(strlist)/2:
#             strlist[i],strlist[len(strlist)-1-i]=strlist[len(strlist)-1-i],strlist[i]
#     # print(strlist)
#     str1 = ''.join(strlist)
#     return str1
# list2 = []
# for i in list1:
#     item = fun(i)
#     list2.append(item)
# print(' '.join(list2)
"""
开发一个注册系统，界面可以用print打印，保存用户名和密码，存在的用户提示已注册，不存在的可以注册成功
解题思路：
    1.打印整个UI界面
    2.选择注册选项，进行判断，用户名是否已经注册
        i.以列表的方式将用户名和密码存储到data.txt文件中
        ii.判断输入的用户名是否存在data.txt中，存在则提示名字已经存在，不存入data.txt中，否则，存入data.txt中
"""
def select_func():
      print('--------请选择功能--------')
      print('1.注册')
      print('0.退出')
def query_user(name):
      list0 = read_file()
      for i in range(len(list0)):
            list2 = eval(list0[i])
            if list2[0] == name:
                  # break
                  return 1
def register():
      name = input('please input your name:')
      psw = input('please input your password:')
      # print(query_user(name))
      if query_user(name) == 1:
            print(f'您输入的用户名{name}已经存在，请重新输入!')
      else:
            list1 = []
            list1.append(name)
            list1.append(psw)
            str1 = str(list1) + '\n'
            write_file(str1)
            print('register sucess!')
def read_file():
      with open('data.txt','r',encoding='utf-8') as f:
            contents = f.readlines()
            return contents
def write_file(str1):
      with open('data.txt','a',encoding='utf-8') as f:
            f.write(str1)
            f.close()
while True:
      select_func()
      num = input('please input your number:')
      if num == '1':
            register()
      if num == '0':
            break



