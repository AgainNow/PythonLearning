#coding:utf-8
'''
学习Python基础语法篇
@author:hekang
'''
import re

#转义字符
print "this is " \
      "the same line"
print 'ab \tac\tad\n' \
      'bb\tbc1\tbd\n' \
      'cb\tcc_1\tcd\n' \
      'db\tdc\t\tdd'
print '----------------------------------------1'

#引号
print ''' 'wo ai '"ni"'''
print "'ni shi ' ''' wo de xiao ping guo '''"
print '''ok ok ok '''
for i in range(5):
    print '*',
print
print '----------------------------------------2'

#类型转换
print int("123")
print str(True)
print str(123)
print bool('')
print '----------------------------------------3'
  
#函数
def hello(a, b = 1, c = 2):
    print "函数:hello,", a, b, c
hello('haha')
hello('haha',3)
hello('haha',c = 3)
print '----------------------------------------4'

#数组操作
list1 = ['mother',15,True]
#查
print '查原数组:',list1
#增
list1.append('Fuck')
print '增append:',list1
list1.insert(2,'hello')
print '增insert',list1
#删
del list1[3]
print '删del:',list1
#改
list1[0] = 'father'
print '改:',list1
#切片,范围[1,3)
print '切片:',list1[1:3]
print '----------------------------------------5'

#字符串切片
sentence1 = 'aaa'
sentence2 = 'I am HanMeiMei '
sentence3 = 'a.b.c.'
print sentence1
print sentence1.split('a')
print sentence2.split()
print sentence3.split('.')
#字符串连接
s1 = '' #相当于连接符
s2 = ';'
list2 = ['mo','th','or']
sentence4 = 'world'
print s1.join(list2)
print s2.join(list2)
print s2.join(sentence4)
print '----------------------------------------6'

#异常处理
try:
    print '异常处理'
except:
    print 'Warning!'
print '----------------------------------------7'

#正则表达式
text1 = "Hi, I am Shirley Hilton. I am his wife."
text2 = "|(021)88776543|010-55667890|02584453362|0571 66345673|(012345678901"
m1 = re.findall(r"\b[Hh]i\b",text1)
m2= re.findall(r"0\d{2}[-]?\d[ ]?\d{7}|(0\d{2})[-]?\d[ ]?\d{7}",text2)
print (m1 and [m1] or ['not match'])[0]
print (m2 and [m2] or ['not match'])[0]
print "\bhi"
print r"\bhi" #r,是raw的意思，它表示对字符串不进行转义
print "\\bhi"
print '----------------------------------------8'

#序列化和反序列化
import time
import cPickle
import pickle #cpickle和pickle功能及用法完全相同,但前者的执行速度是后者的1000倍
startTime = time.time()
#存储
data = ['Save me!', 123.456, True]
# data = "abcdefg" #可行
# data = 15 #可行
f = file("test.data","w")
pickle.dump(data,f)
f.close()
#取存储
f = file("test.data")
data = pickle.load(f)
f.close()
print data
stopTime = time.time()
print stopTime - startTime
print '----------------------------------------9'

list = ['a','b',0]
print ';'.join(str(i) for i in list)

#列表综合/列表解析/列表表达式/List Comprehension
print ';'.join(str(i) for i in range(1,101) if i % 2 == 0 and i % 3 == 0 and i % 5 == 0)
print '----------------------------------------10'

#函数参数传递
def func(a, b = 0, c = 'c'):
    print a,b,c
func(True,c = 'y')
def func2(*args):
    print args
func2(0,1,2,3)
def func3(**kwargs):
    for k in kwargs:
        print k,":",kwargs[k]
func3(hekang = 80,hanmeimei = 85,lilei = 79,)
def func4(x, y = 5, *a, **b): #混合使用
    print x, y, a, b
func4(1)
print '----------------------------------------11'

#lambda表达式
def func(a, b, c):
    return a + b + c
sum = lambda a,b,c:a+b+c
sum2 = lambda a,b,c:func(a,b,c)
print sum(1,2,3)
print sum2(2,3,4)
print '----------------------------------------12'

#全局变量
global x
print '----------------------------------------13'

#map(函数,序列)函数
def func(x = 0):
    return x * 2
list = [1,2,3,4,5,6]
list2 = [2,3,4,5,6,7]
tuple = (1,2,3,4,5,6)
tuple2 = (2,3,4,5,6)
print map(lambda x, y: x + y, list, list2)
print map(lambda i:i * 2, list)
print map(None,tuple)
print map(None, tuple, tuple2)
print map(func,list)
print '----------------------------------------14'

#reduce(函数,序列)函数
print reduce(lambda x,y:x+y,xrange(1,101))

print '----------------------------------------test'
print u'1'
print '\n----------------------------------------0'