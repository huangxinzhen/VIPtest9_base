"""
游戏链接：http://www.hannuota.cn/
视频地址：https://haokan.baidu.com/v?vid=7996301418662973042&pd=bjh&fr=bjhauthor&type=video
解题思路：看视频，跟着画图
"""
i = 0#计数器
def move(n,a,b,c):
    """
    :param n: 盘子数
    :param a: 开始柱
    :param b: 中间柱
    :param c: 目的柱
    :return: 
    """
    global i
    if n == 1:
        i += 1
        print('移动第',i,'次',a,'-->',c)
    else:
        move(n-1,a,c,b)#将a柱子上去盘子通过c柱子移动到b柱子
        move(1,a,b,c)#将a柱子上的盘子通过b柱子移动到c柱子
        move(n-1,b,a,c)#将b柱子上的盘子通过a柱子移动到c柱子
num = int(input('请输入A柱子盘子的个数：'))
print('把',num,'个盘子全部移到C柱子的顺序为：')
move(num,'A','B','C')
