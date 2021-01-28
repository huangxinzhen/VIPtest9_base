#-*- coding:utf-8 -*-


"""
Python练习题：
提示：先去分析要定义的类，属性，方法，对象作为一个参数来传递
1、打印小猫爱吃鱼，小猫要喝水
"""
class Cat():
    def __init__(self,Like,Need):
        self.Like = Like
        self.Need = Need
    def like(self):
        print(f'小猫爱吃{self.Like},小猫需要喝{self.Need}')

cat1 = Cat('鱼','水')
cat1.like()

cat1 = Cat('饭','果汁')
cat1.like()
"""
2、小明爱跑步，爱吃东西。
1）小明体重75.0公斤
2）每次跑步会减肥0.5公斤
3）每次吃东西体重会增加1公斤
4）小美的体重是45.0公斤

思路：
定义一个类为Person
"""
class Person():
    def __init__(self,name,sportType,weight):
        """初始化name,sportType,food,weight"""
        self.name = name
        self.sportType = sportType
        self.weight = weight
    def __str__(self):
        return f'{self.name}体重{self.weight}'
    def sport(self):
        self.weight -= 0.5
        print(f'{self.name}爱{self.sportType},跑步体重变成{self.weight}公斤')
    def eat(self):
        self.weight += 1
        print(f'{self.name}爱{self.sportType},跑步体重变成{self.weight}公斤')
xiaoming = Person('小明','跑步',75.0)
print(xiaoming)
xiaoming.sport()
xiaoming.eat()
xiaoming.eat()

xiaomei = Person('小美','炸鸡',45.0)
print(xiaomei)

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

1.定义房子类：Home，初始化参数area、家具列表furniture
2.定义家具类：Furniture
"""
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
    def add_furniture(self,item):
        """
        添加家具
        :param item: 
        :return: 
        """
        if self.free_area >= item.area:
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
print(home1)
bed = Furniture('床',4)
home1.add_furniture(bed)
print(home1)

wardrobe =Furniture('衣柜',2)
home1.add_furniture(wardrobe)
print(home1)

table = Furniture('餐桌',1.5)
home1.add_furniture(table)
print(home1)


sofa = Furniture('沙发',90)
home1.add_furniture(sofa)
print(home1)
"""
4.士兵开枪
需求：
1）.士兵瑞恩有一把AK47
2）.士兵可以开火(士兵开火扣动的是扳机)
3）.枪 能够 发射子弹(把子弹发射出去)
4）.枪 能够 装填子弹 --增加子弹的数量

思路：
    1.定义一个类：Person，初始变量：身份（identity）、枪（gun）
    2.定义一个类：Gun，定义2个函数，分别为fireBullet（发射子弹）、fillingBullet（填充子弹）

网上百度：  
    1.由于士兵瑞恩有一把AK47，士兵可以开火。故需要先创建枪类
    2.枪类（Gun）：
     （1）属性：型号（model），子弹数目（bullet_count）
     （2）方法：发射子弹（shoot），装填子弹（add_bullet）
    3.士兵类（Soldier）
     （1）属性：姓名（name），枪名（Gun）
     （2）方法：开火（fire）
"""
class Gun():
    """
    枪类，
    属性：星号，子弹数目
    方法：发射子弹，装子弹
    """
    def __init__(self,model,bullet_count):
        """
        :param model: 型号
        :param bullet_count: 子弹数目
        max_bullet_count:最大子弹数目
        """
        self.model = model
        self.bullet_count = bullet_count
        self.max_bullet_count = 10
    #射击方法，在还有子弹的情况下，没射击一次子弹减少一个
    def shoot(self):
        if self.bullet_count > 0:
            self.bullet_count -= 1
        else:
            print(f'没有子弹了，请先安装子弹。')
    #添加子弹的方法，在子弹没有装满的情况下，每次添加一个子弹
    def add_bullet(self):
        if self.bullet_count < self.max_bullet_count:
            self.bullet_count += 1
        else:
            print('子弹已装满')
    #添加子弹方法，在子弹没有装满的情况下，每次装满子弹
    def add_bullet_max(self):
        if self.bullet_count < self.max_bullet_count:
            self.bullet_count += (self.max_bullet_count - self.bullet_count)
        else:
            print('子弹已装满！~~')
class Soldier():
    """
    属性：name,gun名
    方法：开火（fire）
    """
    def __init__(self,name,gun_name):
        self.name = name
        self.gun_name = gun_name
    #开火方法，调用gun里面的射击方法
    def fire(self):
        self.gun_name.shoot()
    #装子弹
    def add_bullets(self):
        self.gun_name.add_bullet_max()
gun01 = Gun('AK47',10)
soldier01 = Soldier('ruien',gun01)
gun01.add_bullet_max()
print(gun01.bullet_count)
soldier01.fire()
soldier01.fire()
print(soldier01.gun_name.bullet_count)
soldier01.add_bullets()
print(soldier01.gun_name.bullet_count)

soldier01.fire()
soldier01.fire()
print(soldier01.gun_name.bullet_count)


# gun01.add_bullet()
# class person():
#     def __init__(self,identity,gun):
#         self.identity = identity
#         self.gun = gun
#     def __str__(self):
#         return f'{self.identity}有一把{self.gun}'
# class Gun(person):
#     def __init__(self,bullet):
#         self.bullet = bullet
#     def fireBullet(self):
#         self.bullet -= 1
#         print(f'发射了{self.bullet}颗子弹')
#     def fillingBullet(self):
#         print(f'填充了{self.bullet}颗子弹')
#
# per = person('士兵','AK47')
# print(per)
# gun = Gun(10)
# gun.fireBullet()
# gun.fillingBullet()