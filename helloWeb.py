#coding:utf-8
import web

urls = (
    '/','index',
	'/movie/(\d+)','movie', #跳转页面
)
#设置数据库连接
db = web.database(
	dbn = 'sqlite',
	db = './helloData/MovieSite.db')
#返回数据
movie = db.select('movie',where = 'id = 1', vars = locals())[0]
print movie
movies = db.select('movie')
print movies[0]['id'],movies[1]['id']
movies = db.select('movie')
print movies[0]['title'],movies[1]['title']
movies = db.select('movie')
print movies[0]['year'],movies[1]['year']
# print movies[0]['title'],movies[0]['year'],movies[0]['country'],movies[0]['abstract']
# movies = [
# 	{
# 		'title': 'Forrest Gump',
# 		'year': 1994,
# 	},
# 	{
# 		'title': 'Titanic',
# 		'year':	1997,
# 	},
# ]

render = web.template.render('templates/') #模板

#处理请求的类movie
class movie:
	def GET(self, movie_id): #访问类似/movie/123的地址时，请求被转到movie中GET方法，而123就成为参数movie_id
		# movie_id = int(movie_id)
		#参数1：表名，参数2：查询条件($movie_id是取变量movie_id的值，参数3：表示参数的来源(所有本地变量))
		condition = 'id = '+movie_id
		movie = db.select('movie',where = condition)[0]
		print movie
		return render.movie(movie)

class index:
    # def GET(self):
    #     return 'Hello,world!'

	# def GET(self):
	# 	page = ''
	# 	for m in movies:
	# 		page += '%s(%d)\n' % (m['title'], m['year'])
	# 	return page

	# def GET(self):
	# 	# page = ''
	# 	# for m in movies:
	# 	# 	page += '%s(%d)\n' % (m['title'], m['year'])
	# 	return render.index(movies)

	def GET(self):
		movies = db.select('movie')
		return render.index(movies)

	def POST(self):
		data = web.input()
		condition = r'title like "%' + data.title + r'%"'
		movies = db.select('movie', where = condition)
		return render.index(movies)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()