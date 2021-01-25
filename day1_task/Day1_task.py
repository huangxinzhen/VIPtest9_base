#-*- coding:utf-8 -*-


"""
Python练习题：
提示：先去分析要定义的类，属性，方法，对象作为一个参数来传递
1、打印小猫爱吃鱼，小猫要喝水
"""
# class Cat():
#     def __init__(self,Like,Need):
#         self.Like = Like
#         self.Need = Need
#     def like(self):
#         print(f'小猫爱吃{self.Like},小猫需要喝{self.Need}')
#
# cat1 = Cat('鱼','水')
# cat1.like()
#
# cat1 = Cat('饭','果汁')
# cat1.like()
"""
2、小明爱跑步，爱吃东西。
1）小明体重75.0公斤
2）每次跑步会减肥0.5公斤
3）每次吃东西体重会增加1公斤
4）小美的体重是45.0公斤

思路：
1.定义一个类为Sports，初始化运动类型：跑步、打球...运动一次，体重减少0.5公斤
2.定义一个类为Love_eat,初始化吃什么东西：炸鸡、烤鸭...每吃一次，体重会增加1公斤
"""
class Sports():
    def __init__(self,name,sportType):
        """初始化name,sportType,food,weight"""
        self.name = name
        self.sportType = sportType
    def sport(self):
        print(f'{self.name}爱{self.sportType}')
class Love_eat():
    def __init__(self,weight,food):
        self.weight = weight
        self.food = food
    def eat(self):
        

"""
3、摆放家具
需求：
1）.房子有户型，总面积和家具名称列表
   新房子没有任何的家具
2）.家具有名字和占地面积，其中
   床：占4平米
   衣柜：占2平面
   餐桌：占1.5平米
3）.将以上三件家具添加到房子中
4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
"""
"""
4.士兵开枪
需求：
1）.士兵瑞恩有一把AK47
2）.士兵可以开火(士兵开火扣动的是扳机)
3）.枪 能够 发射子弹(把子弹发射出去)
4）.枪 能够 装填子弹 --增加子弹的数量
"""