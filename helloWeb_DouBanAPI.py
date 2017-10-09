#coding:utf-8
'''
根据豆瓣API获取250部电影信息，整理好展示在网页中

@author:hekang
'''

import urllib, time, json, web

# #获取电影id
# movie_ids = []
# for index in range(0, 250, 50):
# # for index in range(0, 5):
#     print index
#     #获取数据
#     url = 'http://api.douban.com/v2/movie/top250?start=%d&count=50' % index
#     response = urllib.urlopen(url)
#     data = response.read()
#     # print data
#
#     #数据处理
#     data_json = json.loads(data) #json格式转化为dict对象
#     print data_json
#     movie250 = data_json['subjects']
#     for movie in movie250:
#         movie_ids.append(movie['id'])
#         print movie['id'],movie['title']
#     time.sleep(3)
# print movie_ids
#
# movie_ids = [u'1292052', u'1291546', u'1295644', u'1292720', u'1292063',
#              u'1291546', u'1295644', u'1292720', u'1292063', u'1291561',
#              u'1295644', u'1292720', u'1292063', u'1291561', u'1295124',
#              u'1292720', u'1292063', u'1291561', u'1295124', u'1292722',
#              u'1292063', u'1291561', u'1295124', u'1292722', u'3541415']
#
# #持久化层
#连接数据库
db = web.database(dbn = 'sqlite', db = './helloData/MovieSite.db')
# #数据库_add
# def add_movie(data):
#     movie = json.loads(data)
#     # print 'id = ' + movie['id']
#     # print 'title = ' + movie['title']
#     try:
#         db.insert('movie_douban',
#                   id=int(movie['id']),
#                   title=movie['title'],
#                   origin=movie['original_title'],
#                   url=movie['alt'],
#                   image=movie['images']['large'],
#                   directors=','.join([d['name'] for d in movie['directors']]),
#                   casts=','.join([c['name'] for c in movie['casts']]),
#                   year=movie['year'],
#                   genres=','.join(movie['genres']),
#                   countries=','.join(movie['countries']),
#                   summary=movie['summary'],
#                   )
#     except:
#         print '该条数据有问题:'
#         print movie
#
# #根据取到的电影id取电影信息并储存到数据库
# count = 0
# for mid in movie_ids:
#     url = 'http://api.douban.com/v2/movie/subject/%s' % mid
#     response = urllib.urlopen(url)
#     data = response.read()
#     add_movie(data)
#     count += 1
#     time.sleep(3)

#页面交互
#url映射,范围大的要放后面，不然会被拦截
urls = (
    '/','index_douban', #首页
	'/movie/(.*)','movie_douban', #电影信息页面
    '/cast/(.*)' , 'cast_douban', #演员出演电影列表页面
)

#载入模板
render = web.template.render('templates/')

#首页交互
class index_douban:
    def GET(self):
        movies = db.select('movie_douban')
        count = db.query('SELECT COUNT(*) AS COUNT FROM movie_douban')[0]['COUNT']
        return render.index_douban(movies, count, None)

    def POST(self):
        data = web.input()
        print data
        condition = r'title like "%' + data.title + r'%"'
        movies = db.select('movie_douban', where= condition)
        count = db.query('SELECT COUNT(*) AS COUNT FROM movie_douban WHERE ' + condition)[0]['COUNT']
        print '测试:', count, data.title
        return render.index_douban(movies, count, data.title)

#电影信息页面交互
class movie_douban:
    def GET(self, movie_id):
        condition = 'id = ' + movie_id
        movie = db.select('movie_douban', where = condition)[0]

        return render.movie_douban(movie)

#演员出演电影列表页面交互
class cast_douban:
    def GET(self, cast_name):
        condition = r'casts like "%' + cast_name + r'%"'
        movies = db.select('movie_douban', where = condition)
        print cast_name
        return render.cast_douban(cast_name, movies)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()