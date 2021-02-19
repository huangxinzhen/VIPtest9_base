import os
#删除文件
# os.remove('data_backup.txt')
#删除文件夹
# os.rmdir('test')
#创建文件夹
# os.mkdir('test')
# list1 = os.listdir()
# print(list1)
# os.rename('test.txt','testRename.txt')

#获取当前目录
# dir_name = './'
# print(dir_name)
#
# file_list = os.listdir(dir_name)
# print(file_list)

sep = os.path.sep
# print(sep)
PATH = lambda p:os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)
# print(type(PATH))
# print(PATH)

path = 'D:\\lc\VIPtest9_base\\exam'
print(path)
path = path.replace('\\',sep)
print(path)
# mokeyPath = path + '/..'
# print(mokeyPath)
