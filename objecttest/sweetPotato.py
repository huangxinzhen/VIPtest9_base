#-*- coding:utf -8-*-


class SweetPotato():
    def __init__(self):
        #被烤的时间
        self.cook_time = 0
        #地瓜的状态
        self.cook_static = '生的'
        #调料列表
        self.condiments = []
    def cook(self,time):
        """烤地瓜的方法"""
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_static = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_static = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_static = '熟了'
        elif self.cook_time >= 8:
            self.cook_static = '烤糊了'
    def add_condiments(self,condiment):
        self.condiments.append(condiment)
    def __str__(self):
        return f'这个地瓜烤了{self.cook_time}分钟，状态是{self.cook_static}，添加的调料有{self.condiments}'

digua1 = SweetPotato()
print(digua1)

digua1.cook(2)
digua1.add_condiments('酱油')
print(digua1)


digua1.cook(8)
digua1.add_condiments('辣椒面')
print(digua1)



