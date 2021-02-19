# list1 = [1,2,3,4,6]
# def fun(x,y):
#     return x + y
#     # return x ** 2
# dict1 = {5,4,5,45}
# # result = map(fun,list1)
# # print(result)
# # print(list(result))
# print('##########')
# import functools
# result = functools.reduce(fun,dict1)
# print((result))
#
# def func(x):
#     return x + 2
# dict1 = {5,4,1,45}
# result = map(func,dict1)
# print(result)
# print(set(result))
def fun1(x):
    return x % 2 == 0


list1 = [1,2,3,4,6]
result = filter(fun1,list1)
print(list(result))