#coding:utf-8
'''
Python进阶:操作系统文件
@author:hekang
'''
#读文件
#读取同目录下的文件内容,路径写法还有D:/PythonLearning/data.txt|./data.txt(路径最好用/)
f = file('./helloData/data.txt') #file()和open()是一样的
data1 = f.read()
print 'data1:\n',data1
f.close()

#读取一行内容
f = file('./helloData/data.txt')
print 'data2:'
while True:
      line = f.readline()
      if line:
          print line
      else:
          break
f.close()

#把内容按行读取至一个list中
f = file('./helloData/data.txt')
data3 = f.readlines()
print 'data3:\n',data3
f.close()

#写文件
f = open('./helloData/data_write.txt','w') #会覆盖原内容
f.write('My name is hekang.')
f.close()

f = open('./helloData/data_write.txt','a') #不覆盖原内容，而在结尾添加
f.write('\nHow old are you?')
f.close()

#先读后写,复制操作
f1 = open('./helloData/data.txt','r')
data = f1.read()
# data = f1.readlines() #写法2
f1.close()
f2 = open('./helloData/data_copy.txt','w')
# for line in data: #写法2
    # f2.write(line) #写法2
f2.close()

print '********************************************'
#将data_score.txt中的成绩求均值到新文件中
f1 = open('./helloData/data_score_old.txt','r')
lines = f1.readlines()
print lines
f.close()
result = []
for line in lines:
    info = line.split()
    print info[1:]
    list = []
    for i in info[1:]:
        list.append(float(i))
    print list
    result.append('%s\t%.2f\n'%(info[0],sum(list)/len(list)))
print result
f2 = open('./helloData/data_score_new.txt','w')
f2.writelines(result)
f2.close()

#将数组内容按行写入文件
f = open("./helloData/data_list.txt","w")
list = ["123","Fuck",76,True,[0,1,2,3],(4,5,6,7),{"num1":8, "num2":9}]
for line in list:
    f.write(str(line)+"\n")
f.close()