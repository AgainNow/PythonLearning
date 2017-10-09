#coding:utf-8
'''
查天气小程序
@author: hekang
'''
import urllib2
import json
from city import city

#查天气
cityName = raw_input('你想查哪个城市的天气？\n')
cityCode = city.get(cityName)
if cityCode:
    try:
        url = ('http://www.weather.com.cn/data/cityinfo/%s.html'%cityCode)
        content = urllib2.urlopen(url).read()
        #print content
        data = json.loads(content)
        #print data
        result = data['weatherinfo']
        #print result
        str_temp = ('%s\n%s - %s'%(
            result['weather'],
            result['temp1'],
            result['temp2']
        ))
        print str_temp
    except:
        print '查询失败'
else:
    print '没有找到该城市'

# #获取网页url网络资源
# #url = 'http://www.baidu.com'
# url = 'http://www.weather.com.cn/data/cityinfo/101010100.html'
# web = urllib2.urlopen(url)
# content = web.read()
# print content
# f = open('data.html','w')
# f.write(content)
# f.close()

#自己抓取城市代号列表，得加上try..except...
url1 = 'http://m.weather.com.cn/data3/city.xml'
content1 = urllib2.urlopen(url1).read()
provinces = content1.split(',')
result = 'city = {\n'
for provine in provinces[1:]:
    url2 = 'http://m.weather.com.cn/data3/city%s.xml' % provine.split('|')[0]
    content2 = urllib2.urlopen(url2).read()
    cities = content2.split(',')
    for c in cities:
        url3 = 'http://m.weather.com.cn/data3/city%s.xml'%c.split('|')[0]
        content3 = urllib2.urlopen(url3).read()
        #print content3
        districts = content3.split(',')
        for district in districts:
            url4 = 'http://m.weather.com.cn/data3/city%s.xml'%district.split('|')[0]
            content4 = urllib2.urlopen(url4).read()
            # print content4
            name = district.split('|')[1]
            try:
                code = content4.split('|')[1]
                # print code
            except:
                continue
            line = "    '%s': '%s',\n"%(name, code)
            result += line
result += '}'
f = file('myCity.py','w')
f.write(result)
f.close()
