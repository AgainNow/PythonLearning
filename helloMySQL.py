#coding:utf-8
'''
连接MySQL数据库
'''

import web
import MySQLdb
import pymysql.cursors

#连接数据库
# web自带连接方式,还是得需要安装MySQLdb模块的
# db = web.database(
#     dbn = 'mysql',
#     user = 'root',
#     pw = 'root',
#     db = 'book',
# )

#MySQLdb连接方式
db = MySQLdb.connect(
    host='127.0.0.1',
    user='root',
    passwd='root',
    db='book',
    charset='utf8',
    port=3306
)

#pymysql连接方式
#cursorclass=pymysql.cursors.DictCursor:原本查询到的数据类型是tuple，加了这个就变成了dict
# db = pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='root',
#     db='book',
#     charset='utf8',
#     cursorclass=pymysql.cursors.DictCursor
# )

print db
#操作数据库
#web.py增删改查
# data = db.select('book',where = 'id < 5')
# for d in data:
#     print d.pic
# db.insert('book', pic = '2.jpg', bookname = '中国有嘻哈', author = '小鱼干', publisher = '什么鬼出版社', categoryid = 5)
# updateCount = db.update('book',where='id = 12',categoryid = 6) #返回值是修改的行数
# delCount = db.delete('book',where = 'id = 12')
# print updateCount, delCount
# #直接填sql语句的方式
# data2 = db.query("select * from book where pic = '2.jpg'")
# print data2

#MySQLdbh 和 pymysql增删改查
cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor) #获取一个游标,参数:把tuple类型转化成dict

cursor.execute('select * from book') #执行sql语句
data = cursor.fetchall() #获取查询到的所有行数据
print data[0]
for d in data:
    print d['pic'],d.get('author')
cursor.close() #关闭游标
db.close() #释放数据库资源

# sql = "INSERT INTO book (pic, bookname, author, publisher, categoryid) VALUES (%s, %s, %s, %s, %s)"
# param = ('3.jpg', 'MySQLdb', '55','55',55)
# cursor.execute(sql, param) #单条数据
# cursor.close()
# db.commit() #如果不调用此方法，查询以外的语句不会真正的执行

# sql = 'delete from book where id=11'
# cursor.execute(sql)
# cursor.close()
# db.commit()

# sql = 'update book set pic=%s,author=%s where id=13'
# param = ('6.jpg', '妈妈咪')
# cursor.execute(sql, param)
# cursor.close()
# db.commit()