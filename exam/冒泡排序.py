#-*- coding-utf-8 -*-
list1 = [3,5,1,5,7,0]
n = len(list1)
for i in range(n):
    for j in range(0,n-i-1):
        if list1[j] > list1[j+1]:
            list1[j],list1[j+1] = list1[j+1], list1[j]
print(list1)
for i in list1:
    print(i)

# def bubbleSort(arr):
#     n = len(arr)
#     # 遍历所有数组元素
#     for i in range(n):
#         # Last i elements are already in place
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
# arr = [64, 34, 25, 12, 22, 11, 90]
# bubbleSort(arr)
# print("排序后的数组:")
# for i in range(len(arr)):
#     print("%d" % arr[i]),