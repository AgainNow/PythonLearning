#coding:utf-8
'''
爬虫小程序
通过豆瓣API抓取30部影片的信息
多线程
@author:hekang
'''

import urllib,time,cPickle,thread

time_start = time.time()
data = []

def get_content(i):
    id = 1764796 + i
    url = 'http://api.douban.com/v2/movie/subject/%d' % id
    d = urllib.urlopen(url).read()
    data.append(d)
    print i, time.time() - time_start
    print 'data:', len(data)

for i in xrange(30):
    print 'request movie:',i
    thread.start_new_thread(get_content,(i,))

# f = open('data_movie30.data','w')
# cPickle.dump(data,f)
# f.close()
raw_input('press ENTER to exit..\n') #避免程序提前退出