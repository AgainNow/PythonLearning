#coding:utf-8
'''
根据豆瓣API从豆瓣网获取电影信息并存到数据库
注意：豆瓣GET请求无授权用户每小时只能访问150次，有授权有500次
    movie每分钟能访问40次
'''

import urllib
import json
import time
import web

#获取电影id,写入文本
# movie_ids = []
# for index in xrange(0, 250, 50):
#     print index
#     try:
#         url = 'http://api.douban.com/v2/movie/top250?start=%d&count=50' % index
#         response = urllib.urlopen(url)
#         data = response.read()
#         data_json = json.loads(data)  # json格式转化为dict对象
#         movie250 = data_json['subjects']
#         for movie in movie250:
#             movie_ids.append(movie['id'])
#         time.sleep(3)
#     except:
#         print 'Top250列表请求失败'
#         continue
# f = open('movie_ids.txt','w')
# for movie_id in movie_ids:
#     f.write(str(movie_id)+'\n')
# f.close()

# 读取文件中的movie_ids
movie_ids = []
f = open('movie_ids.txt','r')
lines = f.readlines()
f.close()
for line in lines:
    movie_ids.append(line)
print len(movie_ids), '|', movie_ids
#根据电影id获取电影信息，并转存mysql数据库
db = web.database(dbn='mysql',user = 'root', pw = 'root', db='doubanmovie_top250')
# 将数据填入数据库
def add_movie(data, mid):
    movie = json.loads(data) #json格式转化为dict对象
    try:
        print 'movieId:', movie['id']
        db.insert('movieinfo',
                  id=int(movie['id']),
                  title=movie['title'],
                  original_title=movie['original_title'],
                  year=int(movie['year']),
                  rate=float(movie['rating']['average']),
                  image_small=movie['images']['small'],
                  image_medium=movie['images']['medium'],
                  image_large=movie['images']['large'],
                  subtype=movie['subtype'],
                  genres=','.join(movie['genres']),
                  collect_count=int(movie['collect_count']),
                  cast=','.join(c['id'] for c in movie['casts']),
                  director=','.join(d['id'] for d in movie['directors']),
                  alt=movie['alt'],
                  )
        for cast in movie['casts']:
            print 'castId:', cast['id']
            data = db.select('moviecasts',where = 'id=%d' % int(cast['id']))
            if data:
                continue
            db.insert('moviecasts',
                      id=int(cast['id']),
                      name=cast['name'],
                      alt=cast['alt'],
                      avatars_small=cast['avatars']['small'],
                      avatars_medium=cast['avatars']['medium'],
                      avatars_large=cast['avatars']['large'],
                      )
        for director in movie['directors']:
            print 'directorId:', director['id']
            data = db.select('moviedirectors',where = 'id=%d' % int(director['id']))
            if data:
                continue
            db.insert('moviedirectors',
                      id=int(director['id']),
                      name=director['name'],
                      alt=director['alt'],
                      avatars_small=director['avatars']['small'],
                      avatars_medium=director['avatars']['medium'],
                      avatars_large=director['avatars']['large'],
                      )
    except:
        print '写入数据库失败:', mid, '|', movie
count = 0
for mid in movie_ids:
    print count
    try:
        # 这个网址是怎么来的-------alt------------------------------------------------
        url = 'http://api.douban.com/v2/movie/subject/%s' % mid
        response = urllib.urlopen(url)
        data = response.read()
        count_all = db.query('select count(*) from movieinfo')
        if count_all == 250:
            print '数据库已经有250条数据了'
            break
        data_isHave = db.select('movieinfo', where='id=%d' % int(mid))
        if data_isHave:
            print '该数据已经存在'
            continue
        add_movie(data, mid)
        time.sleep(3)
    except:
        print '获取单条电影信息失败：', mid
    count += 1
    time.sleep(60)

