#coding:utf-8

#汽车与自行车的例子
class Vehicle:#所有车
    def __init__(self,speed):#初始化函数，类属性参数都写在这里，为了在实例化该类时写法简单属性齐全
        self.speed = speed
    def dive(self,distance):
        time = distance / self.speed
        print 'need %.2f hour(s)'%time
class Car(Vehicle):
    def __init__(self, speed, fuel):
        Vehicle.__init__(self,speed)
        self.fuel = fuel
    def dive(self,distance):
        Vehicle.dive(self, distance)
        print 'need %.2f fuels' % (distance * self.speed)
class Bike(Vehicle):
    pass

vehicle = Vehicle(10.0)
print vehicle
#Car
car = Car(150.0, 0.012)
car.dive(100.0)
car.dive(200.0)
#Bike
bike = Bike(15.0)
bike.dive(100.0)
print '-------------------------------------------'

#自己的理解总结
class Father:
  def __init__(self,a='',b=0): #初始化函数,填这个类的属性(域),可以定义属性类型,不定义的话填什么类型都行
    self.a = a
    self.b = b
    self.c = 'c'
  def function1(self,A):
    result = '%s,%s,%d,%s' % (A,self.a,self.b,self.c)
    print result

class Son(Father): #继承
  def __init__(self,a,b,c):
    Father.__init__(self,a,b)
    self.c = c
  def function1(self,A,B): #按需重载该方法
    Father.function1(self,A) #原方法可以保留
    print B,self.c
  def function2(self,C): #添加新方法
    print C
  def function2(self,C='',D=''):
      print C, D

class Daughter(Father): #完全继承，只是改个名字，内容不改
  pass

#引用类的时候
father = Father('a',5)
father.c = 'C'
father.function1('A')
son = Son('a',5,True)
son.function1('A','B')
son.function2('C','D')