#-*- coding:utf-8 -*-

class Home():
    def __init__(self,houseType,area):
        """
        :param houseType: 户型
        :param area: 总面积
        """
        self.houseType = houseType
        self.area = area
        self.free_area = area
        self.furniture = []
    def __str__(self):
        print(f'房子户型是{self.houseType},总面积是{self.area},家具有{self.furniture}')
    def add_furniture(self,item):
        """
        添加家具
        :param item: 
        :return: 
        """
        if self.free_area >= self.area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print(f'{item.name}太大，装不了啦')
    def __str__(self):
        return f'房子的房型是{self.houseType},剩余可用面具{self.free_area},装的家具有{self.furniture}'
class Furniture():
    def __init__(self,name,area):
        """
        :param name: 家具名称
        :param area: 占地面积
        """
        self.name = name
        self.area = area

home1 = Home('三室一厅',90)
bed = Furniture('床',4)
home1.add_furniture(bed)
print(home1)

wardrobe =Furniture('衣柜',2)
home1.add_furniture(wardrobe)
print(home1)

table = Furniture('餐桌',1.5)
home1.add_furniture(table)
print(home1)




