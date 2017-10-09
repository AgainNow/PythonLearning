# coding:utf-8
'''
读取数据库信息，展示在网页上
'''
import web

# url映射
urls = (
    '/', 'index',  # 首页
    '/library/(.*)', 'library', #电影列表
    '/movie/(.*)','movie', #电影信息
    '/cast/(.*)','cast', #演员信息
    '/director/(.*)','director', #导演信息
)
# 载入模板
render = web.template.render('templates/')

# 连接数据库
db = web.database(dbn='mysql', user='root', pw='root', db='doubanmovie_top250')

# 页面交互
class index:
    def GET(self):
        movies = db.select('movieinfo',limit = '0, 20',order = 'rate')
        count = db.query('select count(*) as count from movieinfo')[0]['count']
        return render.index(movies, count, page = 1)

class library:
    def GET(self, page):
        data = web.input()
        start = str((int(page)-1)*24)
        if data:
            condition = r'title like "%' + data.title + r'%"'
            movies = db.select('movieinfo', where = condition,limit =  start + ', 24')
            count = db.query('select count(*) as count from movieinfo where %s'%condition)[0]['count']
            return render.library(movies, count, page, data.title)
        else:
            movies = db.select('movieinfo', limit=start + ', 24')
            count = db.query('select count(*) as count from movieinfo')[0]['count']
            return render.library(movies, count, page, None)
    def POST(self, page):
        data = web.input()
        start = str((int(page) - 1) * 24)
        condition = r'title like "%' + data.title + r'%"'
        movies = db.select('movieinfo', where = condition,limit =  start + ', 24')
        # count = len(movies)
        count = db.query('SELECT COUNT(*) AS COUNT FROM movieinfo WHERE ' + condition)[0]['COUNT']
        return render.library(movies, count, page, data.title)

class movie:
    def GET(self, movie_id):
        movie = db.select('movieinfo', where = 'id = %s' % int(movie_id))[0]
        casts = []
        directors = []
        for cast in movie.cast.split(','):
            data = db.select('moviecasts', where = 'id = %s' % cast)[0]
            casts.append(data)
        for director in movie.director.split(','):
            data = db.select('moviedirectors', where = 'id = %s' % director)[0]
            directors.append(data)
        return render.movie(movie, casts, directors)

class cast:
    def GET(self, cast_id):
        cast = db.select('moviecasts', where = 'id = %s' % cast_id)[0]
        condition = r'cast like "%' + cast_id + r'%"'
        movies = db.select('movieinfo', where = condition)
        return render.character(cast, movies)

class director:
    def GET(self, director_id):
        director = db.select('moviedirectors', where = 'id = %s' % director_id)[0]
        condition = r'director like "%' + director_id + r'%"'
        movies = db.select('movieinfo', where=condition)
        return render.character(director, movies)

if __name__ == '__main__':
    app = web.application(urls, globals())  # 创建一个应用
    app.run()
